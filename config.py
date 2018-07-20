# Default config

class BaseConfig(object):
	DEBUG = True
	SECRET_KEY = '<insert long and secure secret key>'
	SQLALCHEMY_DATABASE_URI = 'postgres://username:password@localhost:5432/database'
