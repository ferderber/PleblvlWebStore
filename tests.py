import unittest

from flask.ext.testing import TestCase

from PleblvlWebStore import Product, User, UserProduct, app, db


class MyTest(TestCase):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = self.SQLALCHEMY_DATABASE_URI
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()
        p = Product(name='Ark Manager')
        db.session.add(p)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_users(self):
        assert True

    def test_add_user_product(self):
        assert True

    def test_add_new_user_product(self):
        user = User(email='test@gmail.com')
        p = Product.query.filter_by(name='Ark Manager').first()
        up = UserProduct(product=p, license='testlicense')
        user.products.append(up)
        db.session.add(user)
        db.session.commit()

        assert True
if __name__ == '__main__':
    unittest.main()
