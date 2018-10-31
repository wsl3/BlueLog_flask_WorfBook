# coding:utf8
# 博客前台
from flask import Blueprint

blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def index():
    return "Hello, index"