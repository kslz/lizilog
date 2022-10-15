# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/10/010 17:45
    @Author : 李子
    @Url : https://github.com/kslz
"""
import os

from flask import Flask

from lizilog.liziprints import auth
from lizilog.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('lizilog')
    app.config.from_object(config[config_name])

    app.register_blueprint(blog)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')
