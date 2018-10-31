# coding:utf8
import os
from flask import Flask, render_template
from config import config
from blueprints.auth import auth_bp
from blueprints.admin import admin_bp
from blueprints.blog import blog_bp
from extensions import db, moment, bootstrap, mail, ckeditor


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "development")

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_logging(app)  # 注册日志处理器
    register_extensions(app)  # 初始化扩展
    register_blueprints(app)  # 注册蓝本
    register_shell_context(app)  # 注册shell上下文处理函数
    register_errorhander(app)  # 注册错误处理函数
    register_commands(app)  # 注册shell自定义命令

    return app


def register_logging(app):
    pass


def register_extensions(app):
    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    ckeditor.init_app(app)


def register_blueprints(app):
    app.register_blueprint(blog_bp)  # 博客前台
    app.register_blueprint(admin_bp, url_prefix="/admin")  # 博客后台
    app.register_blueprint(auth_bp, url_prefix="/auth")  # 用户认证


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_template_context(app):
    pass


def register_errorhander(app):
    @app.errorhandler(400)
    def bad_requests(e):
        return render_template("errors/400.html"), 400


def register_commands(app):
    pass
