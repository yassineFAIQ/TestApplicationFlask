import os
import urllib






class DevelopmentConfig():
    """Env config settings"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///db.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CORS_HEADERS = 'Content-Type'





config_by_name = dict(
    env=DevelopmentConfig
)

