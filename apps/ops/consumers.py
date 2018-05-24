# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-28
# Author Yo
# Email YoLoveLife@outlook.com
from __future__ import absolute_import, unicode_literals
import time
import os,stat
from channels.generic.websocket import WebsocketConsumer
from work.models import Code_Work
from django.conf import settings
from ops.interactive import AnsibleRecvThread

__all__ = [
    "MetaConsumer"
]


class MetaConsumer(WebsocketConsumer):

    def write_key(self, key, file_path):
        try:
            f = open(file_path, 'w')
            f.write(key.private_key)
            f.close()
        except Exception:
            return '~/.ssh/id_rsa'
        os.chmod(file_path,stat.S_IWUSR|stat.S_IRUSR)

        return file_path

    def websocket_receive(self, message):
        pass

    def websocket_disconnect(self, message):
        self.close()

    def websocket_connect(self, message):
        # 接受
        self.accept()
        uuid = self.scope['url_route']['kwargs']['work']

        # 查询必要数据
        work = Code_Work.objects.filter(uuid=uuid).get()
        play_source = work.mission.to_yaml
        vars_dict = work.mission.vars_dict
        inventory = work.mission.group.users_list_byconnectip

        # 创建临时目录
        TMP = settings.OPS_ROOT+str(work.uuid)+'/'
        if not os.path.exists(TMP):
            os.makedirs(TMP)
        vars_dict['BASE'] = TMP

        # 判断该工单是否具备可执行的先决条件
        if work.mission.group.key is not None and work.mission.group.jumper is not None:
            self.write_key(work.mission.group.key, TMP+str(time.time())+'.key')
        else:
            self.send('\r\n您执行的任务缺少必要的密钥或者跳板机请联系管理员解决')
            self.close()

        threadSend = AnsibleRecvThread(work, play_source, inventory, work.mission.group.key, vars_dict, self)
        threadSend.setDaemon = True
        threadSend.start()