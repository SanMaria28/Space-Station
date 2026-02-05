import sqlite3

# Create database connection
conn = sqlite3.connect('space_station.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS crew (
    crew_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    rank TEXT,
    specialization TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS missions (
    mission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mission_name TEXT NOT NULL,
    mission_date TEXT,
    mission_type TEXT,
    description TEXT,
    status TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS crew_missions (
    crew_id TEXT,
    mission_id INTEGER,
    role TEXT,
    PRIMARY KEY (crew_id, mission_id),
    FOREIGN KEY (crew_id) REFERENCES crew(crew_id),
    FOREIGN KEY (mission_id) REFERENCES missions(mission_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS experiments (
    experiment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mission_id INTEGER,
    experiment_name TEXT NOT NULL,
    description TEXT,
    status TEXT,
    results TEXT,
    FOREIGN KEY (mission_id) REFERENCES missions(mission_id)
)
''')

# Insert sample crew members
crew_data = [
    ('CREW001', 'Commander Sarah Chen', 'galaxy123', 'Commander', 'Aerospace Engineering'),
    ('CREW002', 'Dr. James Martinez', 'nebula456', 'Science Officer', 'Astrophysics'),
    ('CREW003', 'Engineer Alex Kim', 'orbit789', 'Flight Engineer', 'Mechanical Engineering'),
    ('CREW004', 'Lt. Emma Johnson', 'stellar321', 'Pilot', 'Navigation'),
    ('CREW005', 'Dr. Ryan Patel', 'cosmos654', 'Medical Officer', 'Space Medicine')
]

cursor.executemany('INSERT OR REPLACE INTO crew VALUES (?, ?, ?, ?, ?)', crew_data)

# Insert sample missions
missions_data = [
    ('Mars Sample Return', '2026-03-15', 'Sample Collection', 'Collect and return geological samples from Mars surface', 'Active'),
    ('ISS Module Installation', '2026-02-28', 'Construction', 'Install new research module on International Space Station', 'Completed'),
    ('Lunar Base Alpha Setup', '2026-04-10', 'Construction', 'Establish first permanent lunar base infrastructure', 'Planned'),
    ('Europa Ice Analysis', '2026-05-20', 'Research', 'Study ice samples from Europa for signs of microbial life', 'Active'),
    ('Solar Observatory Deployment', '2026-01-15', 'Deployment', 'Deploy advanced solar monitoring satellite', 'Completed'),
    ('Asteroid Mining Prep', '2026-06-01', 'Exploration', 'Survey potential asteroid mining sites', 'Planned'),
    ('Deep Space Communication Array', '2026-03-25', 'Installation', 'Install enhanced communication relays for deep space missions', 'Active')
]

cursor.executemany('INSERT INTO missions (mission_name, mission_date, mission_type, description, status) VALUES (?, ?, ?, ?, ?)', 
                  missions_data)

# Insert crew-mission assignments
crew_missions_data = [
    ('CREW001', 1, 'Mission Commander'),
    ('CREW001', 3, 'Mission Commander'),
    ('CREW002', 1, 'Science Lead'),
    ('CREW002', 4, 'Principal Investigator'),
    ('CREW003', 2, 'Lead Engineer'),
    ('CREW003', 3, 'Engineering Lead'),
    ('CREW003', 7, 'Systems Engineer'),
    ('CREW004', 1, 'Pilot'),
    ('CREW004', 6, 'Navigation Officer'),
    ('CREW005', 4, 'Medical Researcher'),
    ('CREW005', 1, 'Medical Officer')
]

cursor.executemany('INSERT INTO crew_missions VALUES (?, ?, ?)', crew_missions_data)

# Insert sample experiments
experiments_data = [
    (1, 'Soil Composition Analysis', 'Analyze Martian soil for mineral content and water traces', 'In Progress', None),
    (1, 'Atmospheric Sampling', 'Collect atmospheric samples at various altitudes', 'Completed', 'CO2 concentration 95.32%, traces of methane detected'),
    (1, 'Rock Core Extraction', 'Extract deep rock cores for age dating', 'Planned', None),
    (2, 'Module Structural Integrity Test', 'Test new module for pressure and structural integrity', 'Completed', 'All tests passed successfully'),
    (2, 'Life Support System Integration', 'Integrate new life support with existing ISS systems', 'Completed', 'Integration successful, all parameters nominal'),
    (3, 'Regolith Construction Tests', 'Test construction techniques using lunar regolith', 'Planned', None),
    (3, 'Water Ice Extraction', 'Develop methods for extracting water from lunar ice deposits', 'Planned', None),
    (4, 'Ice Core Drilling', 'Extract ice cores from Europa surface', 'In Progress', None),
    (4, 'Spectroscopic Analysis', 'Perform spectroscopic analysis of ice samples', 'In Progress', None),
    (4, 'Microbial Life Detection', 'Search for biosignatures in ice samples', 'Planned', None),
    (5, 'Solar Flare Monitoring', 'Monitor and analyze solar flare activity', 'Completed', 'Successfully recorded 23 solar events'),
    (6, 'Mineral Composition Survey', 'Survey asteroid composition for valuable minerals', 'Planned', None),
    (6, 'Trajectory Calculations', 'Calculate optimal mining extraction trajectories', 'Planned', None),
    (7, 'Relay Station Deployment', 'Deploy communication relay stations', 'In Progress', None),
    (7, 'Signal Strength Testing', 'Test signal strength across deep space distances', 'In Progress', None)
]

cursor.executemany('INSERT INTO experiments (mission_id, experiment_name, description, status, results) VALUES (?, ?, ?, ?, ?)', 
                  experiments_data)

conn.commit()
conn.close()

print("Database initialized successfully!")
print("\nSample Login Credentials:")
print("=" * 50)
for crew in crew_data:
    print(f"CrewID: {crew[0]} | Password: {crew[2]} | Name: {crew[1]}")
print("=" * 50)
