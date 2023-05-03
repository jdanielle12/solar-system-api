from app.models.planet import Planet

def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []
    
def test_all_planets_return_a_list_of_planets(client, two_planets):
    response = client.get("/planets")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Jupiter",
        "description": "Jupiter has sixty-seven moons",
        "distance_from_sun": "48.4"
    },
        {
        "id": 2,
        "name": "Mercury",
        "description": "Mercury has zero moons",
        "distance_from_sun": "3.5"
    }]


    
def test_get_one_planet_returns_seeded_planet(client, two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body["id"] == 1
    assert response_body["name"] == "Jupiter"
    assert response_body["description"] == "Jupiter has sixty-seven moons"
    assert response_body["distance_from_sun"] == "48.4"
    
def test_get_one_planets_returns_no_data(client):
    response = client.get("planets/1")
    response_body = response.get_json()
    
    assert response.status_code == 404
    assert response_body == "planet 1 not found"
    
def test_create_planet_happy_path(client):
    EXPECTED_PLANET = {
        "name": "Earth",
        "description": "Earth has one moon",
        "distance_from_sun": "9.3"
    }
    
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_json()
    
    actual_planet = Planet.query.get(1)
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
    assert actual_planet.distance_from_sun == EXPECTED_PLANET["distance_from_sun"]
    