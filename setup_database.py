# setup_database.py
import sqlite3

DATABASE = 'powers.db'

def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS powers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS saved_powers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            power_id INTEGER,
            FOREIGN KEY(power_id) REFERENCES powers(id)
        )
    ''')

    # Insert initial powers
    powers = [
        ('Super Strength', 'Ability to lift and move extremely heavy objects.'),
        ('Flight', 'Ability to fly through the air.'),
        ('Invisibility', 'Ability to become invisible to the naked eye.'),
        ('Telepathy', 'Ability to read and communicate with others through thoughts.'),
        ('Time Travel', 'Ability to travel to different points in time.'),
        ('Teleportation', 'Ability to instantly transport oneself to another location.'),
        ('Fire Control', 'Ability to generate and control fire.'),
        ('Water Manipulation', 'Ability to control and manipulate water.'),
        ('Telekinesis', 'Ability to move objects with the mind.'),
        ('Invulnerability', 'Immunity to physical harm and injury.'),
        ('Super Speed', 'Ability to move at incredibly high speeds.'),
        ('Regeneration', 'Ability to rapidly heal from injuries.'),
        ('Shape-Shifting', 'Ability to change appearance and form at will.'),
        ('Mind Control', 'Ability to influence and control others\' actions.'),
        ('Electrokinesis', 'Ability to generate and control electricity.'),
        ('X-Ray Vision', 'Ability to see through solid objects.'),
        ('Super Intelligence', 'Ability to process information and solve problems with extraordinary speed.'),
        ('Teleportation', 'Ability to transport oneself instantly to different locations.'),
        ('Ice Manipulation', 'Ability to generate and control ice.'),
        ('Animal Communication', 'Ability to communicate with animals.'),
        ('Weather Control', 'Ability to manipulate and control weather patterns.'),
        ('Teleportation', 'Ability to instantly transport oneself to different locations.'),
        ('Molecular Manipulation', 'Ability to alter the molecular structure of objects.'),
        ('Enhanced Senses', 'Heightened senses like sight, hearing, and smell.'),
        ('Super Agility', 'Enhanced agility and reflexes.'),
        ('Shadow Manipulation', 'Ability to control and manipulate shadows.'),
        ('Gravity Control', 'Ability to alter gravitational forces.'),
        ('Elemental Control', 'Ability to control the elements of earth, air, fire, and water.'),
        ('Healing Touch', 'Ability to heal others with touch.')
    ]
    
    cursor.executemany('INSERT INTO powers (name, description) VALUES (?, ?)', powers)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
