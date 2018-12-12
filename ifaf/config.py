#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author  : MG
@Time    : 2018/3/30 17:53
@File    : config.py
@contact : mmmaaaggg@163.com
@desc    :
"""
import logging
from logging.config import dictConfig
from celery.schedules import crontab


# Use a Class-based config to avoid needing a 2nd file
# os.getenv() enables configuration through OS environment variables
class ConfigClass(object):
    # Sql Alchemy settings
    DB_SCHEMA_MD = 'md_integration'
    DB_URL_DIC = {
        # local
        DB_SCHEMA_MD: f"mysql://m*:****@localhost/{DB_SCHEMA_MD}?charset=utf8"
    }

    # log settings
    logging_config = dict(
        version=1,
        formatters={
            'simple': {
                'format': '%(asctime)s %(name)s|%(module)s.%(funcName)s:%(lineno)d %(levelname)s %(message)s'}
        },
        handlers={
            'file_handler':
                {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': 'logger.log',
                    'maxBytes': 1024 * 1024 * 10,
                    'backupCount': 5,
                    'level': 'DEBUG',
                    'formatter': 'simple',
                    'encoding': 'utf8'
                },
            'console_handler':
                {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': 'simple'
                }
        },

        root={
            'handlers': ['console_handler', 'file_handler'],
            'level': logging.DEBUG,
        }
    )
    # logging.getLogger('sqlalchemy.engine').setLevel(logging.WARN)
    dictConfig(logging_config)


config = ConfigClass()
