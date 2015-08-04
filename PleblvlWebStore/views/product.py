from flask import Blueprint, render_template, session, redirect, url_for, \
	request, flash, g, jsonify

mod = Blueprint('product', __name__)

@mod.route('/')
def index():
	return render_template("product/index.html")
