from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
# from flask.ext.migrate import Migrate, MigrateCommand
app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from .models import User, Product, UserProduct
from PleblvlWebStore.views import home
from PleblvlWebStore.views import product
from PleblvlWebStore.views import transaction
from PleblvlWebStore.views import documentation
app.register_blueprint(home.mod)
app.register_blueprint(product.mod, url_prefix='/product')
app.register_blueprint(transaction.mod, url_prefix='/transaction')
app.register_blueprint(documentation.mod, url_prefix='/documentation')
