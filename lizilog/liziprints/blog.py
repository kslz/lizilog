# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/11/011 14:22
    @Author : 李子
    @Url : https://github.com/kslz
"""
from flask import Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    pass