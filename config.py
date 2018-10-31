# coding:utf8
# Flask的配置
import os



class BaseConfig(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "A STRONG SECRET KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv("MEIL_SERVER")
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = ("BlueLog Admin", MAIL_USERNAME)

    BLUELOG_MAIL = os.getenv("BLUELOG_MAIL")
    BLUELOG_POST_PER_PAGE = 10
    BLUELOG_MANAGE_POST_PER_PAGE = 15
    BLUELOG_COMMENT_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    # mysql+pymysql://username:password@localhost:port/database?charset=utf8
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(
        "root", os.getenv("PASSWORD"), "127.0.0.1", "3306", os.getenv("DATABAE")
    )

class TestingConifg(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(
        "root", os.getenv("PASSWORD"), "127.0.0.1", "3306", os.getenv("DATABAE")
    )

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")





config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConifg
}


# 测试是否可以连接数据库
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)
# db = SQLAlchemy(app)

