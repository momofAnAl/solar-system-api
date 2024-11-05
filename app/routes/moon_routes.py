from flask import Blueprint, abort, make_response, request, Response
from app.models.moon import Moon
from app.routes.route_utilities import validate_model
from ..db import db

bp = Blueprint("moon_bp", __name__, url_prefix="/planets/<planet_id>/moons")

@bp.post("")
def create_planet():
    request_body = request.get_json()
    
    try:
        new_moon = Moon.from_dict(request_body)
    
    except KeyError as e:
        Response = {"massage": f"Invalid request:missing{e.args[0]}"}
        abort(make_response, 400)

    db.session.add(new_moon)
    db.session.commit()
    
    response = new_moon.to_dict()
    return response, 201

@bp.get("")
def get_all_moons():
    query = db.select(Moon)
    
    name_param = request.args.get("name")
    if name_param:
        query = query.where(Moon.description.ilike(f"%{name_param}%"))
    
    query = query.order_by(Moon.id)
    
    moons = db.session.scalars(query)
    
    response_body = [moon.to_dict() for moon in planets]
    
    return response_body 
