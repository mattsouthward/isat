import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('FLASK_KEY') or 'KNU3haYVTQtUghFEjf95wpqw5CagWa4vHVjAsEyh'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    ISAT_MAIL_SUBJECT_PREFIX = 'ISAT'
    ISAT_MAIL_SENDER = 'ISAT Admin <isatadmin@atmc.net'
    ISAT_ADMIN = os.environ.get('ISAT_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtpauth.atmc.net'
    MAIL_PORT_TLS = 587
    MAIL_PORT_SSL = 465
    MAIL_USE_SSL_TLS = True
    MAIL_USERNAME = os.environ.get('ISAT_APP_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('ISAT_APP_MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB_URI')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DB_URI')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


config = {
    'development': DevConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevConfig
}
