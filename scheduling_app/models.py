"""Create database models to represent tables."""
from scheduling_app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin

class Load(db.Model):
    """Load model."""
    id = db.Column(db.Integer, primary_key=True)
    load_number = db.Column(db.Integer, nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    shipping_order_number = db.Column(db.Integer, nullable=False)
    customer = db.Column(db.String(80), nullable=False)
    trucker = db.Column(db.String(80), nullable=False)
    pallet_amount = db.Column(db.Integer, nullable=False)
    entered_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    entered_by = db.relationship('User')

class User(UserMixin, db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)