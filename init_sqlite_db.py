import sqlite3

# Create database connection
conn = sqlite3.connect('space_station.db')
cursor = conn.cursor()

# Drop existing tables
cursor.execute('DROP TABLE IF EXISTS experiment')
cursor.execute('DROP TABLE IF EXISTS mission')
cursor.execute('DROP TABLE IF EXISTS crew')

# Create tables matching the MySQL schema
cursor.execute('''
CREATE TABLE crew (
    crew_id INTEGER PRIMARY KEY,
    name VARCHAR(15) NOT NULL,
    role VARCHAR(20),
    nationality VARCHAR(15),
    password VARCHAR(20) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE mission (
    mission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20),
    purpose VARCHAR(20),
    launch_date DATE,
    crew_id INTEGER,
    FOREIGN KEY (crew_id) REFERENCES crew(crew_id)
)
''')

cursor.execute('''
CREATE TABLE experiment (
    experiment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(15),
    field VARCHAR(20),
    status VARCHAR(20),
    mission_id INTEGER,
    crew_id INTEGER,
    FOREIGN KEY (mission_id) REFERENCES mission(mission_id),
    FOREIGN KEY (crew_id) REFERENCES crew(crew_id)
)
''')

# Insert crew data from MySQL dump
crew_data = [
    (1, 'Arjun', 'Commander', 'India', 'pass101'),
    (2, 'Lina', 'Pilot', 'USA', 'pass102'),
    (3, 'Kenji', 'Engineer', 'Japan', 'pass103'),
    (4, 'Maria', 'Scientist', 'Spain', 'pass104'),
    (5, 'Omar', 'Medic', 'UAE', 'pass105'),
    (6, 'Sofia', 'Navigator', 'Brazil', 'pass106'),
    (7, 'Raj', 'Engineer', 'India', 'pass107'),
    (8, 'Emma', 'Scientist', 'UK', 'pass108'),
    (9, 'Noah', 'Tech', 'Canada', 'pass109'),
    (10, 'Chen', 'Researcher', 'China', 'pass110'),
    (11, 'Leo', 'Pilot', 'France', 'pass111'),
    (12, 'Ava', 'Biologist', 'Australia', 'pass112'),
    (13, 'Ivan', 'Engineer', 'Russia', 'pass113'),
    (14, 'Maya', 'Doctor', 'India', 'pass114'),
    (15, 'Lucas', 'Navigator', 'Germany', 'pass115')
]

cursor.executemany('INSERT INTO crew VALUES (?, ?, ?, ?, ?)', crew_data)

# Insert mission data from MySQL dump
missions_data = [
    ('MarsOne', 'PlanetStudy', '2026-03-10', 1),
    ('MoonBase', 'HabitatStudy', '2026-04-15', 4),
    ('AstScan', 'MineralSurvey', '2026-05-20', 7),
    ('SolarX', 'SunObserve', '2026-06-05', 10),
    ('DeepSky', 'GalaxyMap', '2026-07-18', 13)
]

cursor.executemany('INSERT INTO mission (name, purpose, launch_date, crew_id) VALUES (?, ?, ?, ?)', missions_data)

# Insert experiment data from MySQL dump
experiments_data = [
    ('ZeroPlants', 'Biology', 'Active', 1, 2),
    ('MarsSoil', 'Geology', 'Active', 1, 3),
    ('MoonWater', 'Chemistry', 'Done', 2, 5),
    ('MoonRad', 'Physics', 'Active', 2, 6),
    ('AstMetal', 'Chemistry', 'Active', 3, 8),
    ('MineSim', 'Engineering', 'Pending', 3, 9),
    ('SolarTest', 'Physics', 'Active', 4, 11),
    ('DeepSignal', 'Astronomy', 'Active', 5, 14)
]

cursor.executemany('INSERT INTO experiment (title, field, status, mission_id, crew_id) VALUES (?, ?, ?, ?, ?)', 
                  experiments_data)

conn.commit()
conn.close()

print("✅ Database initialized successfully!")
print("\n" + "="*60)
print("SAMPLE LOGIN CREDENTIALS:")
print("="*60)
for crew in crew_data[:10]:
    print(f"CrewID: {crew[0]} | Password: {crew[4]} | Name: {crew[1]} | Role: {crew[2]}")
print("="*60)

print("\n" + "="*60)
print("MISSIONS:")
print("="*60)
for i, mission in enumerate(missions_data, 1):
    print(f"Mission {i}: {mission[0]} - {mission[1]} (Launch: {mission[2]})")
print("="*60)

print("\n🚀 Database ready! Run: python app.py")
