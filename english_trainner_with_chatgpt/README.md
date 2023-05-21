# English Trainner

> English Accompaniment

With ChatGPT, you can improve your English skills in all aspects.

For non-native English-speaking comrades, you can quickly improve your English communication skills.

# Project description

english_trainer_with_chatgpt：项目目录
- models/__init__.py 文件用于存放所有用于 ORM 的模型定义；
- routers/__init__.py 则承建 Flask 应用程序中的所有路由；
- routes/chatbot.py 文件用于定义处理推荐请求的路由；
- templates 目录用于存放 Flask 渲染的 HTML 模板文件；
- gpt.py 文件用于与 OpenAI GPT 3 进行交互；
- app.py 文件用于启动 Flask 聊天机器人应用程序；
- config.py 文件用于存放应用程序的配置变量和 Flask 框架选项； 
tests：测试目录，用于存放单元测试和集成测试的代码

```shell
english_trainer_with_chatgpt/
    english_trainner_with_chatgpt/
        __init__.py
        app.py
        config.py
        gpt.py
        models/
            __init__.py
            english_word.py
            grammar_rule.py
            user.py
        routes/
            __init__.py
            chatbot.py
        templates/
            base.html
    tests/
        unit/
            test_chatbot.py
            __init__.py
    instance/
        config.py
    english_trainer_with_chatgpt.db
    README.md
    requirements.txt
```
说明：
english_trainer_with_chatgpt/：项目根目录。
- english_trainner_with_chatgpt/：包含应用程序代码的 Python 包。
  - __init__.py：应用程序包的入口点，实现了创建 Flask 应用程序的代码。
  - app.py：包含了整个 Flask 应用程序的初始化代码。
  - config.py：包含应用程序所使用的 Flask 和应用程序选项，以及一些默认配置。
  - gpt.py：包含与 OpenAI GPT-3 进行交互的代码。
  - models/：包含用于表示应用程序数据模型的代码。
    - __init__.py：声明应用程序模型包的空文件。
    - english_word.py：定义了 EnglishWord 模型，该模型用于表示英语单词和其定义。
    - grammar_rule.py：定义了 GrammarRule 模型，该模型用于表示语法规则和其解释。
    - user.py：定义了 User 模型，该模型用于表示聊天机器人的用户。
  - routes/：包含用于处理 HTTP 请求的视图函数的代码。
    - __init__.py：声明应用程序路由包的空文件。
    - chatbot.py：定义了用于处理聊天机器人请求的视图函数。
  - templates/：包含应用程序模板的目录。
    - base.html：应用程序的基础 HTML 模板。
- tests/：包含应用程序单元测试的目录。
  - unit/：包含应用程序单元测试用例的目录。
    - test_chatbot.py：定义了针对聊天机器人视图函数的测试用例。
    - __init__.py：声明应用程序测试包的空文件。
- instance/：包含应用程序实例配置文件的目录。
  - config.py：应用程序配置文件的示例。
- english_trainer_with_chatgpt.db：应用程序的 SQLite 数据库文件。
- README.md：应用程序的说明文档。
- requirements.txt：列出了应用程序所依赖的所有 Python 包及其版本号。

# English Trainer with ChatGPT

Welcome to English Trainer with ChatGPT, an open source web application that helps you improve your English skills with the power of GPT.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- Flask SQLAlchemy
- OpenAI API Key (sign up [here](https://beta.openai.com/signup/) to get one)

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/username/repo.git
    cd repo
    ```

2. Create and activate a virtual environment:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Set up the environment variables:

    ```
    export FLASK_APP=english_trainer_with_chatgpt
    export FLASK_ENV=development
    export SECRET_KEY=my_secret_key
    export DATABASE_URL=sqlite:///english_trainer_with_chatgpt.db
    export OPENAI_API_KEY=my_openai_api_key
    ```

5. Run the application:

    ```
    flask run
    ```

6. Open your web browser and navigate to the following URL:

    ```
    http://localhost:5000
    ```

## Usage

1. Open the web application in your web browser.

2. Type in a sentence or a phrase in English that you want to improve.

3. Click the "Ask" button to ask the GPT for a better version of your sentence or phrase.

4. The GPT will return a revised version of your sentence or phrase, which you can use to improve your English skills.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com)
- [OpenAI](https://openai.com)

# English Trainer with ChatGPT

欢迎使用 English Trainer with ChatGPT，一个开源的 Web 应用程序，利用 GPT 的强大功能帮助你提升英语水平。

## 快速入门

### 环境要求

- Python 3.7 及以上版本
- Flask
- Flask SQLAlchemy
- OpenAI API Key（需要先注册 [OpenAI Beta API](https://beta.openai.com/signup/) 并获得 API Key）

### 安装

1. 克隆仓库代码：

    ```
    git clone https://github.com/username/repo.git
    cd repo
    ```

2. 创建并激活 Python 虚拟环境：

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. 安装依赖：

    ```
    pip install -r requirements.txt
    ```

4. 设置环境变量：

    ```
    export FLASK_APP=english_trainer_with_chatgpt
    export FLASK_ENV=development
    export SECRET_KEY=my_secret_key
    export DATABASE_URL=sqlite:///english_trainer_with_chatgpt.db
    export OPENAI_API_KEY=my_openai_api_key
    ```

5. 启动应用：

    ```
    flask run
    ```

6. 在浏览器中打开以下链接：

    ```
    http://localhost:5000
    ```

## 使用方法

1. 在浏览器中打开 Web 应用程序。

2. 输入你想要改进的英语句子或短语。

3. 点击 "Ask" 按钮请求 GPT 返回改进后的版本。

4. GPT 将返回一个改进后的英语句子或短语，你可以使用它来提高自己的英语水平。

## 鸣谢

- [Flask](https://flask.palletsprojects.com)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com)
- [OpenAI](https://openai.com)
