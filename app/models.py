from typing import Any

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base: Any = declarative_base()


class Recipes(Base):
    __tablename__ = 'recipes'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False)
    description = sa.Column(sa.Text)
    instructions = sa.Column(sa.Text)
    created_at = sa.Column(sa.DateTime, server_default='now()')
    updated_at = sa.Column(sa.DateTime)
    ingredients = relationship('Ingredients', backref='recipe', cascade='all, delete-orphan')


class Ingredients(Base):
    __tablename__ = 'ingredients'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    unit = sa.Column(sa.String, nullable=False)
    recipe_id = sa.Column(sa.Integer, sa.ForeignKey('recipes.id'))
    created_at = sa.Column(sa.DateTime, server_default='now()')
    updated_at = sa.Column(sa.DateTime)
