"""
在 app.py 中
定义 Flask 路由和视图函数
实现与 ChatGPT API 的交互
"""
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
app.secret_key = 'dynamic_key'

# 使用 Chat-GPT API 密钥连接到 OpenAI
OPEN_AI_API_KEY = "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"
openai.api_key = OPEN_AI_API_KEY
openai.api_base = "https://api.openai.com/v1"
model_engine = "davinci"


# Flask 定义路由
@app.route('/ask/chatbot', methods=['POST'])
def chatbot():
    # 获取请求的 JSON 数据，此处我们假设此请求 JSON 数据包括 "message" 键
    request_json = request.get_json(silent=True)
    message = request_json['message']

    # 调用 Chat-GPT 生成答案
    response = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=80,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 返回生成的回答
    return jsonify({"response": response.choices[0].text})


@app.route('/ask/question', methods=['POST'])
def inc_question():
    request_json = request.get_json(silent=True)
    question = request_json['question']
    response = openai.Completion.create(
        engine=model_engine,
        prompt=question+"\nAnswer:",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return jsonify({"response": response.choices[0].text})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
