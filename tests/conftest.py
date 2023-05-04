import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_planets(app):
    Jupiter = Planet(
        name="Jupiter",
        description="Jupiter has sixty-seven moons",
        distance_from_sun=48.4
    )
    Mercury = Planet(
        name="Mercury",
        description="Mercury has zero moons",
        distance_from_sun=3.5
    )
    db.session.add(Jupiter)
    db.session.add(Mercury)
    db.session.commit()
