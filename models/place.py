#!/usr/bin/python3
""" this is the place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """public class attributes"""

    city_id: city id
    user_id: user id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids[]
