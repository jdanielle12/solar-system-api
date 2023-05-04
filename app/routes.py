from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

# POST /planets


@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
        db.session.add(new_planet)
        db.session.commit()

        message = jsonify(f"Planet {new_planet.name} successfully created")
        return make_response(message, 201)

    except KeyError as e:
        message = jsonify(f"missing required value: {e}")
        abort(make_response(message, 400))

# GET /planets


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")

    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    results = [planet.to_dict() for planet in planets]

    return jsonify(results)


# GET /planets/<id>

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        message = jsonify(f"{cls.__name__} {model_id} is invalid")
        abort(make_response(message, 400))

    model = cls.query.get(model_id)

    if not model:
        message = jsonify(f"{cls.__name__} {model_id} not found")
        abort(make_response(message, 404))

    return model


@planet_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    planet = validate_model(Planet, id)
    planet_dict = planet.to_dict()

    return planet_dict


# PUT /planets/<id>

@planet_bp.route("/<id>", methods=["PUT"])
def update_one_planet(id):
    planet_data = request.get_json()
    planet_to_update = validate_model(Planet, id)

    planet_to_update.name = planet_data["name"]
    planet_to_update.description = planet_data["description"]
    planet_to_update.distance_from_sun = planet_data["distance_from_sun"]
    db.session.commit()

    message = jsonify(f"Planet {planet_to_update.name} updated")
    return make_response(message, 200)


# DELETE /planets/<id>

@planet_bp.route("/<id>", methods=["DELETE"])
def delete_one_planet(id):
    planet_to_delete = validate_model(Planet, id)
    db.session.delete(planet_to_delete)
    db.session.commit()

    message = jsonify(f"Planet {planet_to_delete.name} deleted")
    return make_response(message, 200)
