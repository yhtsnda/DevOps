# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-5-25
# Author Yo
# Email YoLoveLife@outlook.com

# from pyecharts import Bar
#
# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# # bar.show_config()
# bar.render(path='snapshot.png')


from pyecharts import Pie

ll = [{"name":"CentOS  7.4 64位","value":98},{"name":"CentOS  6.8 64位","value":33},{"name":"CentOS 4/5/6/7 (64 位)","value":407},{"name":"CentOS  7.2 64位","value":94},{"name":"Ubuntu Linux (64 位)","value":41},{"name":"CentOS  6.9 64位","value":20},{"name":"Microsoft Windows Server 2012 (64 位)","value":52},{"name":"Microsoft Windows Server 2008 R2 (64 位)","value":89},{"name":"SUSE Linux Enterprise 11 (64 位)","value":2},{"name":"Ubuntu  14.04 64位","value":2},{"name":"Red Hat Enterprise Linux 6 (64 位)","value":3},{"name":"Windows Server  2008 R2 企业版 64位中文版","value":2},{"name":"Microsoft Windows Server 2008 (64 位)","value":2},{"name":"CentOS  7.3 64位","value":3},{"name":"Microsoft Windows 7 (32 位)","value":13},{"name":"Red Hat Enterprise Linux 5 (64 位)","value":2},{"name":"Microsoft Windows 7 (64 位)","value":3},{"name":"Microsoft Windows Server 2008 (32 位)","value":1},{"name":"Microsoft Windows 8 (64 位)","value":4},{"name":"Microsoft Windows Server 2003 (32 位)","value":3},{"name":"Microsoft Windows Server 2003 Standard (64 位)","value":1},{"name":"其他 2.4.x Linux (32 位)","value":1}]

attr = []
v1 = []

for l in ll:
    attr.append(l["name"])
    v1.append(l["value"])


pie = Pie("123",title_pos='right',width=900)
pie.add("123",attr,v1,center=[50,50],is_random=True,radius=[30,75],is_legend_show=False,is_label_show=True)
pie.show_config()
pie.render(path='sna.png')