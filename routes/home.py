from flask import make_response, jsonify
from flask_restful import Resource


class Home(Resource):
    def get(self):
        return make_response(jsonify({"message": "Nyumbani API"}), 200)
