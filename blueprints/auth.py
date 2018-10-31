# coding:utf8
# 用户认证模块
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login/')
def login():
    return "login"


@auth_bp.route('/logout/')
def logout():
    return "logout"
