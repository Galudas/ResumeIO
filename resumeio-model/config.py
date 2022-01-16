import os

username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')


class DevelopmentConfig:
    DEBUG = True
    DEVELOPMENT = True
    DATABASE_URI = "mongodb://resumeiomodel:resumeiomodel@localhost:27017/admin"
    SQLALCHEMY_DATABASE_URI = "mongodb://localhost:27017/resumeiomodel"


class ProductionConfig:
    DEBUG = False
    TESTING = False
    DATABASE_URI = "mongodb://mongo-root-username:mongo-root-password@resumeio-model-db:27017/mongo-root-db"
    SQLALCHEMY_DATABASE_URI = "mongodb://resumeio-model-db:27017/resumeiomodel"

