class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1a2b3c4d5f@47.97.86.161:3306/flask_db"