import openai


class ChatGPT:
    """
    聊天机器人类，用于调用 OpenAI 的 GPT 模型进行对话生成。
    """
    def __init__(self, api_key):
        """
        初始化 ChatGPT 类的实例。
        """
        openai.api_key = api_key  # 设置 OpenAI 的 API Key
        self.completion_model = "text-davinci-002"  # 指定 GPT 模型
        self.chat_history = []  # 聊天记录列表，用于存储与用户聊天的历史记录。

    def chat(self, message):
        """
        封装了 OpenAI 的生成器，调用 GPT 模型进行对话生成，并将生成的回复返回。
        """
        if message.strip() == '':
            return ''
        prompt = f"{','.join(self.chat_history)} {message.strip()}"  # 拼接输入的消息和历史聊天消息，形成 GPT 模型的输入形式。
        self.chat_history.append(message.strip())  # 将输入的消息添加到聊天历史记录中。
        response = openai.Completion.create(
            engine=self.completion_model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )  # 调用 OpenAI 的生成器 API，使用 GPT 模型生成聊天回复，将回复存储在 response 变量中。
        reply_message = response.choices[0].text.strip()
        self.chat_history.append(reply_message)  # 将生成的回复添加到聊天历史记录中。
        return reply_message
