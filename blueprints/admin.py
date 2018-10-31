# coding:utf8
# 博客后台
from flask import Blueprint

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/")
def admin():
    return "Admin"