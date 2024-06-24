import requests  # Import the requests library to make HTTP requests

# Function to create a new location
def create_location():
    url = 'http://localhost:5000/locations'  # URL endpoint for creating locations
    data = {  # Data to be sent in the POST request
        "LNr": "2",
        "shorttitle": "Forest",
        "description": "A dense forest area"
    }
    response = requests.post(url, json=data)  # Send POST request with data as JSON
    print('Create Location:', response.json())  # Print the response from the server

# Function to update an existing location by ID
def update_location(location_id):
    url = f'http://localhost:5000/locations/{location_id}'  # URL endpoint for updating a specific location
    data = {  # Data to be sent in the PUT request
        "LNr": "updated",
        "shorttitle": "Deep Forest",
        "description": "A very dense forest area"
    }
    response = requests.put(url, json=data)  # Send PUT request with data as JSON
    print('Update Location:', response.json())  # Print the response from the server

# Function to delete a location by ID
def delete_location(location_id):
    url = f'http://localhost:5000/locations/{location_id}'  # URL endpoint for deleting a specific location
    response = requests.delete(url)  # Send DELETE request
    print('Delete Location:', response.json())  # Print the response from the server

# Function to get all locations
def get_locations():
    url = 'http://localhost:5000/locations'  # URL endpoint for getting all locations
    response = requests.get(url)  # Send GET request
    print('Get Locations:', response.json())  # Print the response from the server

# Function to get a specific location by ID
def get_location(location_id):
    url = f'http://localhost:5000/locations/{location_id}'  # URL endpoint for getting a specific location
    response = requests.get(url)  # Send GET request
    print('Get Location:', response.json())  # Print the response from the server

# Function to create a new genus
def create_genus():
    url = 'http://localhost:5000/genus'  # URL endpoint for creating a genus
    data = {  # Data to be sent in the POST request
        "name": "Canis"
    }
    response = requests.post(url, json=data)  # Send POST request with data as JSON
    print('Create Genus:', response.json())  # Print the response from the server

# Function to update an existing genus by ID
def update_genus(genus_id):
    url = f'http://localhost:5000/genus/{genus_id}'  # URL endpoint for updating a specific genus
    data = {  # Data to be sent in the PUT request
        "name": "Felis"
    }
    response = requests.put(url, json=data)  # Send PUT request with data as JSON
    print('Update Genus:', response.json())  # Print the response from the server

# Function to delete a genus by ID
def delete_genus(genus_id):
    url = f'http://localhost:5000/genus/{genus_id}'  # URL endpoint for deleting a specific genus
    response = requests.delete(url)  # Send DELETE request
    print('Delete Genus:', response.json())  # Print the response from the server

# Function to get all genera
def get_genus():
    url = 'http://localhost:5000/genus'  # URL endpoint for getting all genera
    response = requests.get(url)  # Send GET request
    print('Get Genus:', response.json())  # Print the response from the server

# Function to get a specific genus by ID
def get_genus_by_id(genus_id):
    url = f'http://localhost:5000/genus/{genus_id}'  # URL endpoint for getting a specific genus
    response = requests.get(url)  # Send GET request
    print('Get Genus by ID:', response.json())  # Print the response from the server

# Function to create a new animal
def create_animal():
    url = 'http://localhost:5000/animals'  # URL endpoint for creating an animal
    data = {  # Data to be sent in the POST request
        "animal_id": "A001",
        "genus_id": 1,
        "gender": "Male",
        "estimated_size": 1.2,
        "estimated_age": 5,
        "estimated_weight": 35.5
    }
    response = requests.post(url, json=data)  # Send POST request with data as JSON
    print('Create Animal:', response.json())  # Print the response from the server

# Function to update an existing animal by ID
def update_animal(animal_id):
    url = f'http://localhost:5000/animals/{animal_id}'  # URL endpoint for updating a specific animal
    data = {  # Data to be sent in the PUT request
        "animal_id": "updated",
        "genus_id": 1,
        "gender": "Female",
        "estimated_size": 1.1,
        "estimated_age": 4,
        "estimated_weight": 30.0
    }
    response = requests.put(url, json=data)  # Send PUT request with data as JSON
    print('Update Animal:', response.json())  # Print the response from the server

# Function to delete an animal by ID
def delete_animal(animal_id):
    url = f'http://localhost:5000/animals/{animal_id}'  # URL endpoint for deleting a specific animal
    response = requests.delete(url)  # Send DELETE request
    print('Delete Animal:', response.json())  # Print the response from the server

# Function to get all animals
def get_animals():
    url = 'http://localhost:5000/animals'  # URL endpoint for getting all animals
    response = requests.get(url)  # Send GET request
    print('Get Animals:', response.json())  # Print the response from the server

# Function to get a specific animal by ID
def get_animal(animal_id):
    url = f'http://localhost:5000/animals/{animal_id}'  # URL endpoint for getting a specific animal
    response = requests.get(url)  # Send GET request
    print('Get Animal:', response.json())  # Print the response from the server

# Function to create a new observation
def create_observation():
    url = 'http://localhost:5000/observations'  # URL endpoint for creating an observation
    data = {  # Data to be sent in the POST request
        "animal_id": "A001",
        "date": "2023-06-22",
        "time": "14:00",
        "lnr": "LOC001"
    }
    response = requests.post(url, json=data)  # Send POST request with data as JSON
    print('Create Observation:', response.json())  # Print the response from the server

# Function to update an existing observation by ID
def update_observation(observation_id):
    url = f'http://localhost:5000/observations/{observation_id}'  # URL endpoint for updating a specific observation
    data = {  # Data to be sent in the PUT request
        "animal_id": "A001",
        "date": "2023-06-23",
        "time": "15:00",
        "lnr": "LOC002"
    }
    response = requests.put(url, json=data)  # Send PUT request with data as JSON
    print('Update Observation:', response.json())  # Print the response from the server

# Function to delete an observation by ID
def delete_observation(observation_id):
    url = f'http://localhost:5000/observations/{observation_id}'  # URL endpoint for deleting a specific observation
    response = requests.delete(url)  # Send DELETE request
    print('Delete Observation:', response.json())  # Print the response from the server

# Function to get all observations
def get_observations():
    url = 'http://localhost:5000/observations'  # URL endpoint for getting all observations
    response = requests.get(url)  # Send GET request
    print('Get Observations:', response.json())  # Print the response from the server

# Function to get a specific observation by ID
def get_observation(observation_id):
    url = f'http://localhost:5000/observations/{observation_id}'  # URL endpoint for getting a specific observation
    response = requests.get(url)  # Send GET request
    print('Get Observation:', response.json())  # Print the response from the server
