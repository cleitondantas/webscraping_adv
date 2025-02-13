from flask import Flask

from app.controllers.controller import consumer_controller

ACTIVE_ENDPOINTS = (("/",consumer_controller),)
def create_app():
    app = Flask(__name__)

    for url,blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint,url_prefix=url)

    return app