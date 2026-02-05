# 🚀 Space Station Command Center - MySQL Version

A space-themed web application for managing space station missions, crew members, and experiments using MySQL database.

## Prerequisites

1. **MySQL Server** - Install and start MySQL server
   - Download from: https://dev.mysql.com/downloads/mysql/
   - Or install via XAMPP/WAMP
   - Make sure MySQL service is running

2. **Python 3.x** - Already installed

## Installation Steps

### Step 1: Start MySQL Server

Make sure MySQL server is running on localhost:3306

**Using XAMPP:**
- Start XAMPP Control Panel
- Click "Start" for MySQL

**Using MySQL Service:**
```powershell
net start MySQL80
```

### Step 2: Install Python Dependencies

```powershell
cd "c:\Users\sanma\OneDrive\Desktop\DBMS CIA 3"
pip install -r requirements.txt
```

### Step 3: Configure Database Connection

Edit `app.py` and `import_mysql.py` to set your MySQL password:

```python
'password': ''  # Replace with your MySQL root password
```

### Step 4: Import Database

**Option A: Using the import script**
```powershell
python import_mysql.py
```

**Option B: Using MySQL Command Line**
```powershell
mysql -u root -p < space_station.sql
```

**Option C: Using phpMyAdmin (if using XAMPP)**
1. Open http://localhost/phpmyadmin
2. Create database named `space_station`
3. Import the `space_station.sql` file

### Step 5: Run the Application

```powershell
python app.py
```

Then open your browser: http://127.0.0.1:5000

## Sample Login Credentials

Based on the MySQL database:

| CrewID | Password | Name | Role |
|--------|----------|------|------|
| 1 | pass101 | Arjun | Commander |
| 2 | pass102 | Lina | Pilot |
| 3 | pass103 | Kenji | Engineer |
| 4 | pass104 | Maria | Scientist |
| 5 | pass105 | Omar | Medic |
| 6 | pass106 | Sofia | Navigator |
| 7 | pass107 | Raj | Engineer |
| 8 | pass108 | Emma | Scientist |
| 9 | pass109 | Noah | Tech |
| 10 | pass110 | Chen | Researcher |

## Database Schema

### Tables

1. **crew**
   - crew_id (INT, Primary Key, Auto Increment)
   - name (VARCHAR)
   - role (VARCHAR)
   - nationality (VARCHAR)
   - password (VARCHAR)

2. **mission**
   - mission_id (INT, Primary Key, Auto Increment)
   - name (VARCHAR)
   - purpose (VARCHAR)
   - launch_date (DATE)
   - crew_id (INT, Foreign Key → crew)

3. **experiment**
   - experiment_id (INT, Primary Key, Auto Increment)
   - title (VARCHAR)
   - field (VARCHAR)
   - status (VARCHAR)
   - mission_id (INT, Foreign Key → mission)
   - crew_id (INT, Foreign Key → crew)

## Features

- 🏠 **Home Page**: Space-themed landing page
- 🔐 **Login System**: Authenticate using CrewID and Password
- 🎯 **Mission Control**: View all missions and your assigned missions
- 🔬 **Experiments**: View experiments for each mission with crew assignments

## Missions in Database

1. **MarsOne** - PlanetStudy (Launch: 2026-03-10)
2. **MoonBase** - HabitatStudy (Launch: 2026-04-15)
3. **AstScan** - MineralSurvey (Launch: 2026-05-20)
4. **SolarX** - SunObserve (Launch: 2026-06-05)
5. **DeepSky** - GalaxyMap (Launch: 2026-07-18)

## Troubleshooting

### MySQL Connection Error
```
Error: 2003: Can't connect to MySQL server
```
**Solution**: Make sure MySQL server is running

### Access Denied Error
```
Error: 1045: Access denied for user 'root'
```
**Solution**: Update the password in `app.py` and `import_mysql.py`

### Database Not Found
```
Error: 1049: Unknown database 'space_station'
```
**Solution**: Run `import_mysql.py` or manually import the SQL file

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: MySQL 8.0
- **Frontend**: HTML, CSS (space theme)
- **Authentication**: Flask sessions
- **Dependencies**: scikit-learn, numpy, mysql-connector-python

Enjoy exploring the cosmos! 🌌
