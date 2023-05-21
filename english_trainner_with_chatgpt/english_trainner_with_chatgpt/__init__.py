from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 导入视图模块
from english_trainner_with_chatgpt.routes import *

# 创建 Flask 实例
app = Flask(__name__)

# 配置 Flask 实例
app.config.from_object('config.ProductionConfig')

# 创建 SQLAlchemy 实例
db = SQLAlchemy(app)
