from flask import Blueprint, jsonify, abort, make_response,request
from app.models.moon import Moon
from app import db
from helper import validate_model

moon_bp = Blueprint("moons", __name__, url_prefix="/moons")

@moon_bp.route("", methods=["POST"])
def create_moon():
    request_body = request.get_json()
    try:
        new_moon = Moon.from_dict(request_body)
    
        db.session.add(new_moon)
        db.session.commit()
    
        message = jsonify(f"Moon {new_moon.id} successfully created")
        return make_response(message, 201)
    
    except KeyError as e:
        abort(make_response(jsonify(f"missing required value: {e}"), 400))
        
@moon_bp.route("", methods=["GET"])
def get_all_moons():
    moons = Moon.query.all()
    results = []
    for moon in moons:
        results.append(moon.to_dict())
    return jsonify(results)


@moon_bp.route("/<id>", methods=["GET"])
def get_one_moon(id):
    moon = validate_model(Moon, id)
    moon_dict = moon.to_dict()

    return moon_dict


