"""App configuration."""
from os import environ
import os


class Config:
    """Set Flask configuration vars from environment variables."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Flask-SQLAlchemy
    #SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # GCP
    GOOGLE_APPLICATION_CREDENTIALS = 'key.json'
    CLOUDSQL_USER = 'mainuser'
    CLOUDSQL_PASSWORD = 'test123'
    CLOUDSQL_DATABASE = 'app_db'
    CLOUDSQL_CONNECTION_NAME = 'fourth-flag-270813:us-central1:attendance-database'
    LOCAL_SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{nam}:{pas}@127.0.0.1:3306/{dbn}').format (
        nam=CLOUDSQL_USER,
        pas=CLOUDSQL_PASSWORD,
        dbn=CLOUDSQL_DATABASE,
    )

    LIVE_SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{nam}:{pas}@localhost/{dbn}?unix_socket=/cloudsql/{con}').format (
        nam=CLOUDSQL_USER,
        pas=CLOUDSQL_PASSWORD,
        dbn=CLOUDSQL_DATABASE,
        con=CLOUDSQL_CONNECTION_NAME,
    )
    if os.environ.get ('GAE_INSTANCE'):
        SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
    else:
        SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI