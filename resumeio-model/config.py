import os


class DevelopmentConfig:
    DEBUG = True
    DEVELOPMENT = True
    DATABASE_URI = "mongodb://resumeiomodel:resumeiomodel@localhost:27017/admin"
    SQLALCHEMY_DATABASE_URI = "mongodb://localhost:27017/resumeiomodel"


class ProductionConfig:
    DEBUG = False
    TESTING = False
    DATABASE_URI = "mongodb://cmVzdW1laW9tb2RlbA==:cmVzdW1laW9tb2RlbA==@resumeio-model-db:27017/admin?authSource=admin"
    SQLALCHEMY_DATABASE_URI = "mongodb://resumeio-model-db:27017/cmVzdW1laW9tb2RlbA=="

