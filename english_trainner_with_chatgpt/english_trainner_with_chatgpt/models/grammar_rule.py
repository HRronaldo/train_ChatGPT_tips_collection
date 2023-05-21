from english_trainner_with_chatgpt import db


class GrammarRule(db.Model):
    """
    GrammarRule: 用于保存语法规则和其解释
    __tablename__: 指定了模型在数据库中使用的表名
    id: 是一个自增主键
    rule: 存储语法规则本身
    explanation: 存储与规则相关的解释
    """
    __tablename__ = "grammar_rule"

    id = db.Column(db.Integer, primary_key=True)
    rule = db.Column(db.String(500), nullable=False)
    explanation = db.Column(db.String(1000))

    def __repr__(self):
        return f"<GrammarRule {self.rule}>"
