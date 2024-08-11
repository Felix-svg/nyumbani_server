from flask import jsonify, make_response
from flask_restful import Resource
from models.property import Property
from utils.errors import server_error, not_found


class Listings(Resource):
    def get(self):
        try:
            listings = [
                property.to_dict(rules=["-contact"])
                for property in Property.query.all()
            ]

            return make_response(jsonify(listings), 200)
        except Exception as e:
            return server_error(e)


class ListingByID(Resource):
    def get(self, id):
        try:
            listing = Property.query.filter_by(id=id).first()
            if not listing:
                return not_found("Listing")

            listing_dict = listing.to_dict(rules=["-contact"])
            return make_response(jsonify(listing_dict), 200)
        except Exception as e:
            return server_error(e)
