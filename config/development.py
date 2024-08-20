from .default import Config
import os
from datetime import timedelta

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://theyoonicon:yaudrl8735@localhost/pado'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # 토큰 만료 시간 설정
