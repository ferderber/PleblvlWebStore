import os

import stripe
from flask import (Blueprint, flash, g, jsonify, redirect, render_template,
                   request, session, url_for)

from PleblvlWebStore import db
from PleblvlWebStore.models import Product, User, UserProduct

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
    print(request.values)
    customer = stripe.Customer.create(
        email=request.values['email'],
        card=request.values['id']
    )
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='cad',
        description='Pleblvl Software'
    )
    u = User.query.filter_by(email=request.values['email']).first()
    p = Product.query.filter_by(name='Ark Manager').first()
    userProduct = UserProduct(product=p, license='123')
    if u is None:
        u = User(request.values['email'])
        u.products.append(userProduct)
        db.session.add(u)
    else:
        u.products.append(userProduct)
    db.session.commit()
    return render_template('transaction/charge.html', amount=amount / 100)

# Using this route to test for now
@mod.route('/charge2')
def test():
    print(request.cookies)
    return render_template('transaction/charge.html', amount=amount / 100)
