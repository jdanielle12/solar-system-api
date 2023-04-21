from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, distance_from_earth):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_earth = distance_from_earth
        
planets = [Planet(1, "Mercury", "Mercury has zero moons", 3.5), 
           Planet(2, "Venus", "Venus has zero moons", 6.7),
           Planet(3, "Earth", "Earth has one moon", 9.3),
           Planet(4, "Mars", "Mars has two moons", 14.2),
           Planet(5, "Jupiter", "Jupiter has sixty-seven moons", 48.4),
           Planet(6, "Saturn", "Saturn has sixty-two moons", 88.9),
           Planet(7, "Uranus", "Uranus has twenty-seven moons", 179),
           Planet(8, "Neptune", "Neptune has fourteen moons", 288),
           Planet(9, "Pluto", "Pluto has five moons", 367)
]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    all_planets_response = []
    for planet in planets:
        all_planets_response.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            distance_from_earth=planet.distance_from_earth
        ))
    return jsonify(all_planets_response)
