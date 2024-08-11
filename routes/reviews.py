from flask import request, make_response, jsonify
from flask_restful import Resource
from models.review import Review
from config import db
from utils.errors import server_error, not_found, no_input_data, missing_fields, create


class Reviews(Resource):
    from flask import request, make_response, jsonify


from flask_restful import Resource
from models.review import Review
from config import db
from utils.errors import server_error, not_found, no_input_data, missing_fields, create


class Reviews(Resource):
    def get(self):
        try:
            house_id = request.args.get("houseId")
            if not house_id:
                return not_found("House")

            reviews = Review.query.filter_by(house_id=house_id).all()
            if not reviews:
                # Return an empty list instead of an error when no reviews are found
                return make_response(jsonify([]), 200)

            reviews_list = [review.to_dict() for review in reviews]
            return make_response(jsonify(reviews_list), 200)
        except Exception as e:
            return server_error(e)

    def post(self):
        try:
            data = request.get_json()
            if not data:
                return no_input_data()

            house_id = data.get("houseId")
            review_text = data.get("review")

            if not house_id or not review_text:
                return missing_fields()

            review = Review(house_id=house_id, review=review_text)
            db.session.add(review)
            db.session.commit()
            return create("Review")
        except Exception as e:
            db.session.roll()
            return server_error(e)
