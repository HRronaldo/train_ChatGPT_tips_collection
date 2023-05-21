from english_trainner_with_chatgpt import db


class EnglishWord(db.Model):
    """
    EnglishWord : 它将表示英语单词和其定义
    __tablename__: 指定了模型在数据库中使用的表名
    id: 是一个自增主键
    word: 存储单词本身
    definition: 存储与单词相关的定义
    """
    __tablename__ = "english_word"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.String(500))

    def __repr__(self):
        return f"<EnglishWord {self.word}>"
