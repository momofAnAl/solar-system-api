from sqlalchemy.orm import Mapped, mapped_column
from app.db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter: Mapped[int] #in kilometers
    number_of_moons: Mapped[int]
    
    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["diameter"] = self.diameter
        planet_as_dict["number_of_moons"] = self.number_of_moons

        return planet_as_dict
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name=planet_data["name"],
            description=planet_data["description"],
            diameter=planet_data["diameter"],
            number_of_moons=planet_data["number_of_moons"]
        )






