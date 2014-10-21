import os

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')

class Development(Config):
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave'
class Testing(Config):
	TESTING = True

class Production(Config):
	pass	

config = {
	'development': Development,
	'testing': Testing,
	'production': Production,

	'default': Development
}