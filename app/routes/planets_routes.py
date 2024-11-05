from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.routes.route_utilities import validate_model
from ..db import db

bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()
    
    try:
        new_planet = Planet.from_dict(request_body)
    
    except KeyError as e:
        Response = {"massage": f"Invalid request:missing{e.args[0]}"}
        abort(make_response, 400)

    db.session.add(new_planet)
    db.session.commit()
    
    response = new_planet.to_dict()
    return response, 201
    
@bp.get("")
def get_all_planets():
    query = db.select(Planet)
    
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    number_of_moons_param = request.args.get("number_of_moons")
    if number_of_moons_param:
        query = query.where(Planet.number_of_moons == number_of_moons_param)
       
    query = query.order_by(Planet.id)
    
    planets = db.session.scalars(query)
    
    response_body = [planet.to_dict() for planet in planets]
    
    return response_body 

@bp.get("/<planet_id>")
def get_single_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()

@bp.put("/<planet_id>")
def update_single_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]
    planet.number_of_moons = request_body["number_of_moons"]

    db.session.commit()

    return Response(status=204, mimetype='application/json')

@bp.delete("/<planet_id>")
def delete_single_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype='application/json')


