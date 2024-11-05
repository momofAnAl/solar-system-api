from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from sqlalchemy import ForeignKey
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size_in_km: Mapped[int]
    description: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")
    
    def to_dict(self):
        moon_as_dict = {}
        moon_as_dict["id"] = self.id
        moon_as_dict["name"] = self.name
        moon_as_dict["size_in_km"] = self.size_in_km
        moon_as_dict["description"] = self.description
        
        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        new_moon = cls(id=moon_data["id"], 
                       name=moon_data["name"],
                       size_in_km=moon_data["size_in_km"],
                       description=moon_data["description"])
        
        return new_moon
        