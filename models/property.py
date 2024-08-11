from config import db
from sqlalchemy_serializer import SerializerMixin


class Property(db.Model, SerializerMixin):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    type = db.Column(db.String(50))
    price = db.Column(db.String(50))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    city = db.Column(db.String(100))
    square_footage = db.Column(db.Integer)
    image = db.Column(db.String)

    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'))
    contact = db.relationship('ContactInformation', back_populates='properties')
    
    # Store property features as a JSON array
    property_features = db.Column(db.JSON, nullable=False)
