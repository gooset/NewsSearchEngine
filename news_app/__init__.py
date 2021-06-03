from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ec9439tfc6c796ae2029594d'

from news_app import routes
