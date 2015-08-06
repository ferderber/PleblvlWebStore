from . import db


userProducts = db.Table('userProducts',
                        db.Column('user_id', db.Integer,
                                  db.ForeignKey('user.id')),
                        db.Column('product_id', db.Integer,
                                  db.ForeignKey('product.id')),
                        db.Column('license', db.String(36))
                        )


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(256), unique=True)
  products = db.relationship('Product', secondary=userProducts,
                             backref=db.backref('users', lazy='dynamic'))

  def __init__(self, email):
    self.email = email

  def __repr__(self):
    return '<User %r>' % self.email


class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(50))

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return '<Product %r>' % self.name


# class UserProduct(db.Model):
#   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#   product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#
#   def __init__(self, user_id, product_id):
#     self.user_id = user_id
#     self.product_id = product_id
#
#   def __repr__(self):
#     return '<UserProduct %r>' % self.id
