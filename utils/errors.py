from flask import jsonify, make_response


def not_found(model_instance):
    return make_response(jsonify({"error": f"{model_instance} not found"}), 404)


def no_input_data():
    return make_response(jsonify({"error": "No input data provided"}), 400)


def missing_fields():
    return make_response(jsonify({"error": "missing required fields"}), 400)


def server_error(e):
    return make_response(jsonify({"error": "Internal Server Error: " + str(e)}), 500)


def create(model_instance):
    return make_response(
        jsonify({"message": f"{model_instance} created successfully"}), 201
    )


def update(model_instance):
    return make_response(
        jsonify({"message": f"{model_instance} updated successfully"}), 200
    )


def delete(model_instance):
    return make_response(
        jsonify({"message": f"{model_instance} deleted successfully"}), 200
    )
