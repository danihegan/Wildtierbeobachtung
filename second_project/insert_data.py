from flask import Flask, request, jsonify, render_template, flash  # Import necessary modules from Flask
import sqlite3  # Import sqlite3 for database operations
from create_db import create_database  # Import the create_database function
app = Flask(__name__)  # Create a Flask application instance

# Function to execute a database query and return the results
def query_db(query, args=(), one=False):
    con = sqlite3.connect('database.db')  # Connect to the SQLite database
    cur = con.cursor()  # Create a cursor object
    cur.execute(query, args)  # Execute the query with the given arguments
    rv = cur.fetchall()  # Fetch all results
    con.close()  # Close the database connection
    return (rv[0] if rv else None) if one else rv  # Return one result or all results based on 'one' parameter

# Function to modify the database (insert, update, delete)
def modify_db(query, args=()):
    con = sqlite3.connect('database.db')  # Connect to the SQLite database
    cur = con.cursor()  # Create a cursor object
    cur.execute(query, args)  # Execute the query with the given arguments
    con.commit()  # Commit the changes
    con.close()  # Close the database connection

@app.route('/')  # Route for the home page
@app.route('/index')  # Alternative route for the home page
def index():
    return render_template('index.html')  # Render the index.html template

@app.route('/create_location', methods=['GET', 'POST'])  # Route for creating a location
def create_location():
    if request.method == 'POST':  # Check if the request method is POST
        data = request.form  # Get form data
        modify_db('INSERT INTO Location (LNr, shorttitle, description) VALUES (?, ?, ?)',
                  (data['lnr'], data['shorttitle'], data.get('description', '')))  # Insert data into Location table
        return render_template('create_location.html')  # Render the create_location.html template
    return render_template('create_location.html')  # Render the create_location.html template for GET requests

@app.route('/create_genus', methods=['GET', 'POST'])  # Route for creating a genus
def create_genus():
    if request.method == 'POST':  # Check if the request method is POST
        data = request.form  # Get form data
        modify_db('INSERT INTO Genus (name) VALUES (?)', (data['name'],))  # Insert data into Genus table
        return render_template('create_genus.html')  # Render the create_genus.html template
    return render_template('create_genus.html')  # Render the create_genus.html template for GET requests

@app.route('/create_animal', methods=['GET', 'POST'])  # Route for creating an animal
def create_animal():
    if request.method == 'POST':  # Check if the request method is POST
        data = request.form  # Get form data
        modify_db('''
            INSERT INTO Animal (animal_id, genus_id, gender, estimated_size, estimated_age, estimated_weight)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (data['id'], data['genus_id'], data['gender'], data['estimated_size'], data['estimated_age'], data['estimated_weight']))  # Insert data into Animal table
        genera = query_db('SELECT * FROM Genus')  # Query all genera
        return render_template('create_animal.html', genera=genera)  # Render the create_animal.html template with genera data
    genera = query_db('SELECT * FROM Genus')  # Query all genera
    return render_template('create_animal.html', genera=genera)  # Render the create_animal.html template with genera data for GET requests

@app.route('/create_observation', methods=['GET', 'POST'])  # Route for creating an observation
def create_observation():
    if request.method == 'POST':  # Check if the request method is POST
        data = request.form  # Get form data
        modify_db('''
            INSERT INTO Observation (animal_id, date, time, lnr)
            VALUES (?, ?, ?, ?)''',
            (data['animal_id'], data['date'], data['time'], data['lnr']))  # Insert data into Observation table
        animals = query_db('SELECT * FROM Animal')  # Query all animals
        locations = query_db('SELECT * FROM Location')  # Query all locations
        return render_template('create_observation.html', animals=animals, locations=locations)  # Render the create_observation.html template with animals and locations data

    animals = query_db('SELECT * FROM Animal')  # Query all animals
    locations = query_db('SELECT * FROM Location')  # Query all locations
    return render_template('create_observation.html', animals=animals, locations=locations)  # Render the create_observation.html template with animals and locations data for GET requests

if __name__ == '__main__':
    create_database()  # Call the create_database function to initialize the database
    app.run(debug=True, port=8000)  # Run the Flask application with debug mode enabled on port 8000
