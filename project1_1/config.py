import os


class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY')
    # Configure session to use filesystem
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"