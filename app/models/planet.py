from app import db
from helper import validate_model

class Planet(db.Model):
    id = db.Column(
            db.Integer,
            primary_key=True,
            autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    distance_from_sun = db.Column(db.String, nullable=False)
    moons = db.relationship("Moon", back_populates="planet")
    
    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "distance_from_sun": self.distance_from_sun
        }
        
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
                name = data_dict["name"],
                description = data_dict["description"],
                distance_from_sun = data_dict["distance_from_sun"]
        )
        
