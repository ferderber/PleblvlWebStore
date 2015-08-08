from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(256), unique=True)
    products = db.relationship('UserProduct', backref='users')
    # def __init__(self, email):
    #   self.email = email
    #
    # def __repr__(self):
    #   return '<User %r>' % self.email


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    # def __init__(self, name):
    #   self.name = name
    #
    # def __repr__(self):
    #   return '<Product %r>' % self.name


class UserProduct(db.Model):
    __tablename__ = 'user_products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), primary_key=True)
    product = db.relationship('Product', backref="userproducts")
    license = db.Column(db.String(26))
    # def __init__(self, user_id, product_id):
    #   self.user_id = user_id
    #   self.product_id = product_id
    #
    # def __repr__(self):
    #   return '<UserProduct %r>' % self.id
