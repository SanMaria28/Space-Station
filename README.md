# 🚀 Space Station Command Center

A beautiful space-themed Streamlit web application for managing space station missions, crew members, and experiments.

## Application
The application was deployed via streamlit.io

[Space Station Command Center](https://space-stationgit-jfewdrr9jdx93fratbbz8g.streamlit.app/)

## Features

- 🏠 **Home Page**: Beautiful space-themed landing page with animated stars and floating planets
- 🔐 **Login System**: Secure authentication using CrewID and Password
- 🎯 **Mission Control**: View all missions and your assigned missions
- 🔬 **Experiments**: Detailed view of experiments for each mission
- 👨‍🚀 **Crew Management**: Track crew members and their roles
- ✨ **Modern UI**: Smooth animations, hover effects, and gradient designs

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize the database:
```bash
python init_sqlite_db.py
```

This will create the SQLite database with sample data including:
- 15 crew members
- 5 missions
- 8 experiments

## Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. The app will automatically open in your browser at:
```
http://localhost:8501
```

## Sample Login Credentials

| Role | Crew ID | Password | Name |
|------|---------|----------|------|
| Commander | 1 | pass101 | Arjun |
| Pilot | 2 | pass102 | Lina |
| Engineer | 3 | pass103 | Kenji |
| Scientist | 4 | pass104 | Maria |
| Medic | 5 | pass105 | Omar |

## Application Structure

```
Space-Station/
├── app.py                  # Main Streamlit application
├── init_sqlite_db.py       # Database initialization script
├── requirements.txt        # Python dependencies
├── space_station.db        # SQLite database (created after init)
├── space_station.sql       # SQL schema reference
└── LICENSE                 # License file
```

## Database Schema

### Tables

1. **crew**: Stores crew member information
   - crew_id (Primary Key)
   - name
   - role
   - nationality
   - password

2. **mission**: Stores mission details
   - mission_id (Primary Key)
   - name
   - purpose
   - launch_date
   - crew_id (Foreign Key)

3. **experiment**: Stores experiment information
   - experiment_id (Primary Key)
   - title
   - field
   - status
   - mission_id (Foreign Key)
   - crew_id (Foreign Key)

## Features Overview

### Home Page
- Animated stars background
- Floating planets
- Feature cards with hover effects
- Mission statistics display
- Call-to-action buttons

### Login Page
- Centered authentication card
- Pulsing lock icon animation
- Sample credentials display
- Secure session management

### Mission Control Page
- View your assigned missions
- Browse all space station missions
- Color-coded status badges
- Mission cards with smooth hover effects
- Direct links to experiment details

### Experiments Page
- View all experiments for a specific mission
- Experiment cards with status indicators
- Summary data table
- Back navigation to missions

## Technologies Used

- **Framework**: Streamlit (Python web framework)
- **Database**: SQLite
- **Frontend**: Custom CSS with space theme
- **Data Display**: Pandas DataFrames
- **Authentication**: Streamlit session state
- **Dependencies**: streamlit, pandas, numpy

## Design Features

- ✨ Animated scrolling stars background
- 🌍 Floating planets with rotation animation
- 🎨 Gradient color scheme (cyan #00d4ff and green #00ff88)
- 💫 Smooth hover effects and transitions
- 🎴 Status badges with different colors
- 📱 Responsive design
- 🔝 Sticky navigation bar

## Notes

- The application uses Streamlit session state for authentication
- Database is automatically created with sample data
- All pages feature a beautiful space-themed design
- Fully responsive and works on various screen sizes
- Real-time page updates with Streamlit's reactive model

Enjoy exploring the cosmos! 🌌
