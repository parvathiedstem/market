from market import bcrypt
from market import db



class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(length=30), unique=True, nullable=False)
    email_address = db.Column(db.String(length=50), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.String(length=50), nullable=False, default=1000)
    items = db.relationship('Item', backref="owned_user", lazy=True)
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Item(db.Model):
    name = db.Column(db.String(length=30), unique=True, nullable=False)
    id = db.Column(db.Integer(), primary_key=True)
    barcode = db.Column(db.String(length=20), unique=True, nullable=False)
    price = db.Column(db.Integer(), unique=True, nullable=False)
    Description = db.Column(db.String(length=1024), unique=True, nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
