from flask import Flask, request, jsonify  # Import necessary modules from Flask
import sqlite3  # Import sqlite3 for database operations
from create_db import create_database  # Import the create_database function
app = Flask(__name__)  # Create a Flask application instance

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')  # Connect to the SQLite database
    conn.row_factory = sqlite3.Row  # Configure to return rows as dictionaries
    return conn

@app.route('/locations', methods=['POST'])  # Route for creating a location
def create_location():
    data = request.get_json()  # Get JSON data from the request
    lnr = data['LNr']  # Extract LNr from the data
    shorttitle = data['shorttitle']  # Extract shorttitle from the data
    description = data.get('description')  # Extract description from the data

    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('INSERT INTO Location (LNr, shorttitle, description) VALUES (?, ?, ?)',
                   (lnr, shorttitle, description))  # Insert data into Location table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Location created successfully'}), 201  # Return success message

@app.route('/locations/<id>', methods=['PUT'])  # Route for updating a location
def update_location(id):
    data = request.get_json()  # Get JSON data from the request
    lnr = data['LNr']  # Extract LNr from the data
    shorttitle = data['shorttitle']  # Extract shorttitle from the data
    description = data.get('description')  # Extract description from the data

    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('UPDATE Location SET LNr = ?, shorttitle = ?, description = ? WHERE LNr = ?',
                   (lnr, shorttitle, description, id))  # Update the Location table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Location updated successfully'}), 200  # Return success message

@app.route('/locations/<id>', methods=['DELETE'])  # Route for deleting a location
def delete_location(id):
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('DELETE FROM Location WHERE LNr = ?', (id,))  # Delete from Location table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Location deleted successfully'}), 200  # Return success message

@app.route('/genus', methods=['POST'])  # Route for creating a genus
def create_genus():
    data = request.get_json()  # Get JSON data from the request
    name = data['name']  # Extract name from the data

    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('INSERT INTO Genus (name) VALUES (?)', (name,))  # Insert data into Genus table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Genus created successfully'}), 201  # Return success message

@app.route('/genus/<id>', methods=['PUT'])  # Route for updating a genus
def update_genus(id):
    data = request.get_json()  # Get JSON data from the request
    name = data['name']  # Extract name from the data

    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('UPDATE Genus SET name = ? WHERE id = ?', (name, id))  # Update the Genus table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Genus updated successfully'}), 200  # Return success message

@app.route('/genus/<id>', methods=['DELETE'])  # Route for deleting a genus
def delete_genus(id):
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('DELETE FROM Genus WHERE id = ?', (id,))  # Delete from Genus table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Genus deleted successfully'}), 200  # Return success message

@app.route('/animals', methods=['POST'])  # Route for creating an animal
def create_animal():
    data = request.get_json()  # Get JSON data from the request
    animal_id = data['animal_id']  # Extract animal_id from the data
    genus_id = data['genus_id']  # Extract genus_id from the data
    gender = data['gender']  # Extract gender from the data
    estimated_size = data['estimated_size']  # Extract estimated_size from the data
    estimated_age = data['estimated_age']  # Extract estimated_age from the data
    estimated_weight = data['estimated_weight']  # Extract estimated_weight from the data

    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('''
        INSERT INTO Animal (animal_id, genus_id, gender, estimated_size, estimated_age, estimated_weight)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (animal_id, genus_id, gender, estimated_size, estimated_age, estimated_weight))  # Insert data into Animal table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Animal created successfully'}), 201  # Return success message

@app.route('/animals/<id>', methods=['PUT'])  # Route for updating an animal
def update_animal(id):
    data = request.get_json()  # Get JSON data from the request
    animal_id = data['animal_id']  # Extract animal_id from the data
    genus_id = data['genus_id']  # Extract genus_id from the data
    gender = data['gender']  # Extract gender from the data
    estimated_size = data['estimated_size']  # Extract estimated_size from the data
    estimated_age = data['estimated_age']  # Extract estimated_age from the data
    estimated_weight = data['estimated_weight']  # Extract estimated_weight from the data

    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('''
        UPDATE Animal
        SET animal_id = ?, genus_id = ?, gender = ?, estimated_size = ?, estimated_age = ?, estimated_weight = ?
        WHERE animal_id = ?
    ''', (animal_id, genus_id, gender, estimated_size, estimated_age, estimated_weight, id))  # Update the Animal table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Animal updated successfully'}), 200  # Return success message

@app.route('/animals/<id>', methods=['DELETE'])  # Route for deleting an animal
def delete_animal(id):
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('DELETE FROM Animal WHERE animal_id = ?', (id,))  # Delete from Animal table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Animal deleted successfully'}), 200  # Return success message

@app.route('/observations', methods=['POST'])  # Route for creating an observation
def create_observation():
    data = request.get_json()  # Get JSON data from the request
    animal_id = data['animal_id']  # Extract animal_id from the data
    date = data['date']  # Extract date from the data
    time = data['time']  # Extract time from the data
    lnr = data['lnr']  # Extract lnr from the data

    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('''
        INSERT INTO Observation (animal_id, date, time, lnr)
        VALUES (?, ?, ?, ?)
    ''', (animal_id, date, time, lnr))  # Insert data into Observation table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Observation created successfully'}), 201  # Return success message

@app.route('/observations/<id>', methods=['PUT'])  # Route for updating an observation
def update_observation(id):
    data = request.get_json()  # Get JSON data from the request
    animal_id = data['animal_id']  # Extract animal_id from the data
    date = data['date']  # Extract date from the data
    time = data['time']  # Extract time from the data
    lnr = data['lnr']  # Extract lnr from the data

    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('''
        UPDATE Observation
        SET animal_id = ?, date = ?, time = ?, lnr = ?
        WHERE id = ?
    ''', (animal_id, date, time, lnr, id))  # Update the Observation table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Observation updated successfully'}), 200  # Return success message

@app.route('/observations/<id>', methods=['DELETE'])  # Route for deleting an observation
def delete_observation(id):
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('DELETE FROM Observation WHERE id = ?', (id,))  # Delete from Observation table
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

    return jsonify({'message': 'Observation deleted successfully'}), 200  # Return success message

@app.route('/locations', methods=['GET'])  # Route for getting all locations
def get_locations():
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM Location')  # Query all locations
    locations = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the database connection

    return jsonify([dict(ix) for ix in locations]), 200  # Return locations data

@app.route('/locations/<id>', methods=['GET'])  # Route for getting a location by ID
def get_location(id):
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM Location WHERE LNr = ?', (id,))  # Query location by LNr
    location = cursor.fetchone()  # Fetch one result
    conn.close()  # Close the database connection

    if location is None:  # Check if location is not found
        return jsonify({'message': 'Location not found'}), 404  # Return not found message

    return jsonify(dict(location)), 200  # Return location data

@app.route('/genus', methods=['GET'])  # Route for getting all genus
def get_genus():
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM Genus')  # Query all genus
    genus_list = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the database connection

    return jsonify([dict(ix) for ix in genus_list]), 200  # Return genus data

@app.route('/genus/<id>', methods=['GET'])  # Route for getting a genus by ID
def get_genus_by_id(id):
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM Genus WHERE id = ?', (id,))  # Query genus by ID
    genus = cursor.fetchone()  # Fetch one result
    conn.close()  # Close the database connection

    if genus is None:  # Check if genus is not found
        return jsonify({'message': 'Genus not found'}), 404  # Return not found message

    return jsonify(dict(genus)), 200  # Return genus data

@app.route('/animals', methods=['GET'])  # Route for getting all animals
def get_animals():
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM Animal')  # Query all animals
    animals = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the database connection

    return jsonify([dict(ix) for ix in animals]), 200  # Return animals data

@app.route('/animals/<id>', methods=['GET'])  # Route for getting an animal by ID
def get_animal(id):
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM Animal WHERE animal_id = ?', (id,))  # Query animal by ID
    animal = cursor.fetchone()  # Fetch one result
    conn.close()  # Close the database connection

    if animal is None:  # Check if animal is not found
        return jsonify({'message': 'Animal not found'}), 404  # Return not found message

    return jsonify(dict(animal)), 200  # Return animal data

@app.route('/observations', methods=['GET'])  # Route for getting all observations
def get_observations():
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM Observation')  # Query all observations
    observations = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the database connection

    return jsonify([dict(ix) for ix in observations]), 200  # Return observations data

@app.route('/observations/<id>', methods=['GET'])  # Route for getting an observation by ID
def get_observation(id):
    conn = get_db_connection()  # Get a database connection
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('SELECT * FROM Observation WHERE id = ?', (id,))  # Query observation by ID
    observation = cursor.fetchone()  # Fetch one result
    conn.close()  # Close the database connection

    if observation is None:  # Check if observation is not found
        return jsonify({'message': 'Observation not found'}), 404  # Return not found message

    return jsonify(dict(observation)), 200  # Return observation data

if __name__ == '__main__':
    create_database()  # Call the create_database function to initialize the database
    app.run(debug=True, port=5000)  # Run the Flask application with debug mode enabled on port 5000
