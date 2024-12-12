import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import date

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    created_at = Column(Date, default=date.today)
    favorite_planets = relationship('FavoritePlanets', backref="user")
    favorite_characters = relationship('FavoriteCharacters', backref="user")


class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    ability = Column(String(250))


class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    home_planet = relationship('Planets', backref="characters")


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
