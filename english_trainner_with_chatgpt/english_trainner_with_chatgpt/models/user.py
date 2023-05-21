from english_trainner_with_chatgpt import db


class User(db.Model):
    """
    User: 用于保存聊天机器人的用户和其密码哈希
    __tablename__: 指定了模型在数据库中使用的表名
    id: 是一个自增主键
    username: 存储用户名
    password_hash: 存储经过哈希处理的密码
    email: 用户的电子邮件列，且具有唯一约束。
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return f"<User {self.username}>"
