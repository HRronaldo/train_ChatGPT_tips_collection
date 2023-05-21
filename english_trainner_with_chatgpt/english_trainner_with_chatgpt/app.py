import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from english_trainner_with_chatgpt.gpt import ChatGPT

# 导入应用程序所需的模型类
from english_trainner_with_chatgpt.models.user import User
from english_trainner_with_chatgpt.models.english_word import EnglishWord
from english_trainner_with_chatgpt.models.grammar_rule import GrammarRule

# 导入所有的蓝图对象，用于区分路由和视图函数
from english_trainner_with_chatgpt.routes.main import main_bp
from english_trainner_with_chatgpt.routes.auth import auth_bp
from english_trainner_with_chatgpt.routes.chatbot import chatbot_bp


# 创建 Flask 应用对象，并从 config.py 文件中读取配置
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')
app.config.from_pyfile('config.py', silent=True)

# 创建 SQLAlchemy 的实例，并与 Flask 应用程序进行关联
db = SQLAlchemy(app)

# 创建聊天机器人 ChatGPT 的实例，并使用 os.getenv() 方法获取 OpenAI API Key
chatbot = ChatGPT(os.getenv('OPENAI_API_KEY', ''))

# 将蓝图对象注册到应用程序中
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(chatbot_bp)

if __name__ == '__main__':
    # 运行 Flask 应用程序
    app.run()
