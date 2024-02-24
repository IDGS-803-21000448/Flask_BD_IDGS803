import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'mi clave secreta'
    SESION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

