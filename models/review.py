from config import db
from sqlalchemy_serializer import SerializerMixin

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    review = db.Column(db.Text, nullable=False)