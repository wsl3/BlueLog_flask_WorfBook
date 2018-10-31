# coding:utf8
# 模型设计
from extensions import db
from datetime import datetime


# 管理员
class Admin(db.Model):
    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(100))
    name = db.Column(db.String(30))
    about = db.Column(db.Text)


# 文章分类
class Category(db.Model):
    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    posts = db.relationship("Post", back_populates="category")


# 文章
class Post(db.Model):
    id = db.Column(db.interger, primary_key=True, autoincreament=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Interger, db.ForeignKey("category.id"))
    category = db.relation("Category", back_populates="post")
    comments = db.relationship("Comment", back_populates="post", cascade="all")


# 评论
class Comment(db.Model):
    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(255))
    site = db.Column(db.String(255))
    body = db.Column(db.Text)
    from_admin = db.Column(db.Boolean, default=False)
    reviewed = db.Column(db.Boolean, default=False)
    timestrap = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    post_id = db.Column(db.Interger, db.ForeignKey("post.id"))
    post = db.relationship("Post", back_populates="comments")

    # 评论的回复
    replied_id = db.Column(db.Interger, db.ForeignKey("comment.id"))
    replied = db.relationship("Comment", back_populates="replies", remote_side=[id])
    replies = db.relationship("Comment", back_populates="replied", cascade="all")
