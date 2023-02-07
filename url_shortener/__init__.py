from flask import Flask

def create_app():
	app = Flask(__name__, instance_relative_config=False)

	from . import service
	app.register_blueprint(service.bp)

	return app
