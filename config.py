
class Config(object):
    DEBUG = False
    TESTING = False

    SERCRET_KEY = "\xf3\xc4]B'\xc7\x915f\x818\xc4N8Ak&\xba\x18}\xfe\x0b\xf3\xd0"

    DB_HOST = "ec2-3-218-171-44.compute-1.amazonaws.com"
    DB_NAME = "ddd4mnclae5h30"
    DB_USER = "atwrtaatphuwev"
    DB_PASS = "bbe8f3b93fd8c58cb9ac8c952b4cd9daf74edd1454bec9d83088aaad2d889788"

    UPLOADS = "/Users/new/PycharmProjects/inventarizaciya_final/app/static/img"

    SESSION_COOKIE_SECURE = True
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_HOST = "ec2-3-218-171-44.compute-1.amazonaws.com"
    DB_NAME = "ddd4mnclae5h30"
    DB_USER = "atwrtaatphuwev"
    DB_PASS = "bbe8f3b93fd8c58cb9ac8c952b4cd9daf74edd1454bec9d83088aaad2d889788"
    SERCRET_KEY = "\xf3\xc4]B'\xc7\x915f\x818\xc4N8Ak&\xba\x18}\xfe\x0b\xf3\xd0"
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False