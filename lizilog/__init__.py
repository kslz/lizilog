# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/10/010 17:37
    @Author : 李子
    @Url : https://github.com/kslz
"""
import os

from flask import Flask


from lizilog.liziprints import auth, blog, admin
from lizilog.liziprints.admin import admin_bp
from lizilog.liziprints.auth import auth_bp
from lizilog.liziprints.blog import blog_bp
from lizilog.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('lizilog')
    app.config.from_object(config[config_name])

    register_blueprints(app)

def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')
