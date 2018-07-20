from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)

import chatbot


if __name__ == "__main__":
    app.run()