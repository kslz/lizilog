# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/11/011 9:12
    @Author : 李子
    @Url : https://github.com/kslz
"""
from flask import Blueprint

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login')
def login():
    pass

@auth_bp.route('/logout')
def logout():
    pass
