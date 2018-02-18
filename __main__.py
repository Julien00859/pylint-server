from flask import Flask
from os import environ
from pylint_server import mainbp

app = Flask("pylint-server")
app.register_blueprint(mainbp)
app.run(host=environ.get("PYLINT_SERVER_HOST", "127.0.0.1"), port=int(environ.get("PYLINT_SERVER_PORT", 5001))
