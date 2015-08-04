from flask import Blueprint, render_template, session, redirect, url_for, \
	request, flash, g, jsonify
import stripe, os

# Amount in cents
amount = 2000
stripe_keys = {
    'secret_key': os.environ['STRIPE_SECRET_KEY'],
    'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']
mod = Blueprint('transaction', __name__)

@mod.route('/')
def index():
	return render_template('transaction/index.html', key=stripe_keys['publishable_key'], amount=amount)
@mod.route('/charge', methods=['POST'])
def charge():
	print(request.cookies)
	customer = stripe.Customer.create(
		email=request.form['stripeEmail'],
		card=request.form['stripeToken']
	)
	charge = stripe.Charge.create(
		customer=customer.id,
		amount=amount,
		currency='cad',
		description='Pleblvl Software'
	)
	return render_template('transaction/charge.html', amount=amount / 100)
