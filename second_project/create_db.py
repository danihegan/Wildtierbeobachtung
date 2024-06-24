import sqlite3


def create_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Tabellen erstellen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Location (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LNr TEXT NOT NULL,
            shorttitle TEXT NOT NULL,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Genus (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Animal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal_id TEXT,
            genus_id INTEGER,
            gender TEXT,
            estimated_size REAL,
            estimated_age REAL,
            estimated_weight REAL,
            FOREIGN KEY (genus_id) REFERENCES Genus(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Observation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal_id TEXT,
            date TEXT,
            time TEXT,
            lnr TEXT,
            FOREIGN KEY (animal_id) REFERENCES Animal(id),
            FOREIGN KEY (lnr) REFERENCES Location(LNr)
        )
    ''')

    connection.commit()
    connection.close()

