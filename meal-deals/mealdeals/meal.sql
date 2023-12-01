CREATE DATABASE recipe_app;
USE recipe_app;

CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ingredients TEXT NOT NULL,
    preparation_time INT NOT NULL,
    recipe TEXT NOT NULL
);
