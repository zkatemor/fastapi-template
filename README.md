# Recipe API

> I asked СhatGPT to describe the terms of reference for an educational project on Fast API, here is the result.

## Technical Specification for Recipe API Service

The Recipe API Service is a web application built on Fast API that provides information on recipes. The application will use a PostgreSQL database with a simple structure of two tables: "recipes" and "ingredients". The "recipes" table will store information about each recipe, including its name, instructions, and a foreign key reference to the "ingredients" table. The "ingredients" table will store information about each ingredient, including its name.

```
 CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  instructions TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ingredients (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  unit TEXT NOT NULL,
  recipe_id INTEGER REFERENCES recipes(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

## The API will have the following endpoints:

- **GET** /recipes: Returns a list of all recipes with their names and instructions.
- **GET** /recipes/{id}: Returns the details of a specific recipe, including its name, instructions, and ingredients.
- **POST** /recipes: Creates a new recipe with its name, instructions, and a list of ingredients.
- **PUT** /recipes/{id}: Updates the details of a specific recipe, including its name, instructions, and ingredients.
- **DELETE** /recipes/{id}: Deletes a specific recipe.

The API service will be built using Python and the Fast API framework. The database will be PostgreSQL, and the application will use SQLAlchemy to interact with the database. The API will be secured with authentication and authorization using OAuth 2.0.

Overall, the Recipe API Service is a simple, yet useful application that allows users to retrieve, create, update, and delete recipes and their associated ingredients.
