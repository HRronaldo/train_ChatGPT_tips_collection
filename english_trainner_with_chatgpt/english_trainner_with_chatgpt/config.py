import os


class Config:
    """
    配置基类，包含共有的 Flask 配置信息。
    """
    
    # 调试模式
    DEBUG = False

    # 数据库 URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///english_trainer_with_chatgpt.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 密钥和加密方式
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT', 'my_security_salt')

    # OpenAI 的 API Key
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')


class ProductionConfig(Config):
    """
    生产环境配置，继承了 Config 基类。
    """
    
    # 生产环境下关闭调试模式
    DEBUG = False


class DevelopmentConfig(Config):
    """
    开发环境配置，继承了 Config 基类。
    """
    
    # 开发环境下启用调试模式
    DEBUG = True


class TestingConfig(Config):
    """
    测试环境配置，继承了 Config 基类。
    """
    
    # 开启测试模式
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'  # 使用内存数据库

    # 关闭 CSRF 保护
    WTF_CSRF_ENABLED = False
