from app import db

class Moon(db.Model):
    id = db.Column(
            db.Integer,
            primary_key=True,
            autoincrement=True)
    size = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    fun_fact = db.Column(db.String, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="moons")
   
    
    def to_dict(self):
        return {
                "id": self.id,
                "size": self.size,
                "description": self.description,
                "fun_fact": self.fun_fact
        }
        
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
                size = data_dict["size"],
                description = data_dict["description"],
                fun_fact = data_dict["fun_fact"]
        )
        
