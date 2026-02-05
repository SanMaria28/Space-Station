# 🚀 Space Station Command Center

A space-themed web application for managing space station missions, crew members, and experiments.

## Features

- 🏠 **Home Page**: Beautiful space-themed landing page
- 🔐 **Login System**: Secure authentication using CrewID and Password
- 🎯 **Mission Control**: View all missions and assigned missions
- 🔬 **Experiments**: Detailed view of experiments for each mission
- 👨‍🚀 **Crew Management**: Track crew members and their roles

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize the database:
```bash
python init_db.py
```

This will create the SQLite database with sample data including:
- 5 crew members
- 7 missions
- Multiple experiments
- Crew-mission assignments

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Sample Login Credentials

| Role | CrewID | Password |
|------|--------|----------|
| Commander Sarah Chen | CREW001 | galaxy123 |
| Dr. James Martinez | CREW002 | nebula456 |
| Engineer Alex Kim | CREW003 | orbit789 |
| Lt. Emma Johnson | CREW004 | stellar321 |
| Dr. Ryan Patel | CREW005 | cosmos654 |

## Application Structure

```
DBMS CIA 3/
├── app.py                  # Main Flask application
├── init_db.py             # Database initialization script
├── requirements.txt       # Python dependencies
├── space_station.db       # SQLite database (created after init_db.py)
└── templates/
    ├── base.html          # Base template with navigation
    ├── index.html         # Home page
    ├── login.html         # Login page
    ├── missions.html      # Missions listing page
    └── experiments.html   # Experiments detail page
```

## Database Schema

### Tables

1. **crew**: Stores crew member information
   - crew_id (Primary Key)
   - name
   - password
   - rank
   - specialization

2. **missions**: Stores mission details
   - mission_id (Primary Key)
   - mission_name
   - mission_date
   - mission_type
   - description
   - status

3. **crew_missions**: Links crew members to missions
   - crew_id (Foreign Key)
   - mission_id (Foreign Key)
   - role

4. **experiments**: Stores experiment information
   - experiment_id (Primary Key)
   - mission_id (Foreign Key)
   - experiment_name
   - description
   - status
   - results

## Features Overview

### Navigation Bar
- **Home**: Return to landing page
- **Login**: Authenticate crew members
- **Missions**: View all missions (requires login)
- **Logout**: End session

### Mission Page
- View all space station missions
- See missions assigned to logged-in crew member
- Each mission displays:
  - Mission name and status
  - Date and type
  - Description
  - Link to view experiments

### Experiments Page
- View all experiments for a specific mission
- Experiment details include:
  - Name and ID
  - Description
  - Status (Planned, In Progress, Completed)
  - Results (if available)

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite
- **Frontend**: HTML, CSS (with space theme)
- **Authentication**: Flask sessions
- **Dependencies**: scikit-learn (as requested), numpy

## Notes

- The application uses session-based authentication
- Database is automatically created with sample data
- All pages feature a beautiful space-themed design with animated stars
- Responsive design works on various screen sizes

Enjoy exploring the cosmos! 🌌
