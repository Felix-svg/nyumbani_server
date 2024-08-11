from config import db
from sqlalchemy_serializer import SerializerMixin


class ContactInformation(db.Model, SerializerMixin):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    # One-to-many relationship
    properties = db.relationship("Property", back_populates="contact")
