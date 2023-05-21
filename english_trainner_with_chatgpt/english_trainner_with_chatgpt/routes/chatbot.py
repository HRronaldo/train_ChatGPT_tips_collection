"""
实现 learn（语言学习）接口
"""
import os
from flask import Blueprint, jsonify, request
from english_trainner_with_chatgpt.gpt import ChatGPT

bp = Blueprint("chatbot", __name__)
chatbot = ChatGPT(os.getenv("OPENAI_API_KEY"))


@bp.route("/")
def index():
    """
    index 方法用于测试应用程序是否正常工作
    :return:
    """
    return "Chatbot is running..."


@bp.route("/chatbot")
def chatbot_route():
    """
    chatbot_route 方法用于向用户介绍聊天机器人
    :return:
    """
    return "Hey there, I'm a chatbot! Ask me something."


@bp.route("/chatbot/api", methods=["POST"])
def chatbot_api():
    """
    chatbot_api 方法用于处理推荐请求
    chatbot_api 方法首先将请求中的 JSON 数据进行解析，
    然后使用 GPT 3 模型生成响应文本。
    最终将响应文本存储在 JSON 格式中，然后返回给客户端。
    """
    # 尝试从请求中获取 JSON 格式数据
    try:
        data = request.get_json()
        message = data["message"]
    # 如果获取失败则返回错误
    except Exception as e:
        return jsonify({'code': 400, 'message': str(e)})
    # 使用 Chatbot 对象生成响应
    response = chatbot.generate_response(message)
    # 将响应数据封装为 JSON 格式并返回
    return jsonify({'code': 200, 'response': response})
