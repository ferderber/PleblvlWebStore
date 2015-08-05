from flask import (Blueprint, flash, g, jsonify, redirect, render_template,
                   request, session, url_for)

mod = Blueprint('product', __name__)

@mod.route('/')
def index():
	return render_template("product/index.html")
