# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-5-30
# Author Yo
# Email YoLoveLife@outlook.com
enable_utc = False
timezone = 'Asia/Shanghai'
broker_url = "redis://:@localhost:6379/3"
# result_backend = "redis://:@localhost:6379/3"
task_serializer = 'pickle'
result_serializer = 'pickle'
accept_content = ['json', 'pickle']
# worker_log_format = '%(message)s'
# worker_task_log_format = '%(message)s'
# task_eager_propagates = True
# worker_redirect_stdouts = True
# worker_redirect_stdouts_level = "INFO"
# worker_hijack_root_logger = False