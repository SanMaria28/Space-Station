import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import os

# Database initialization function
def init_database():
    """Initialize the database with sample data if it doesn't exist"""
    if not os.path.exists('space_station.db'):
        conn = sqlite3.connect('space_station.db')
        cursor = conn.cursor()
        
        # Create tables
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
        
        # Insert crew data
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
        
        # Insert mission data
        missions_data = [
            ('MarsOne', 'PlanetStudy', '2026-03-10', 1),
            ('MoonBase', 'HabitatStudy', '2026-04-15', 4),
            ('AstScan', 'MineralSurvey', '2026-05-20', 7),
            ('SolarX', 'SunObserve', '2026-06-05', 10),
            ('DeepSky', 'GalaxyMap', '2026-07-18', 13)
        ]
        cursor.executemany('INSERT INTO mission (name, purpose, launch_date, crew_id) VALUES (?, ?, ?, ?)', missions_data)
        
        # Insert experiment data
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

# Initialize database on app startup
init_database()

# Page configuration
st.set_page_config(
    page_title="Space Station Command",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS matching the original Flask design exactly
st.markdown("""
<style>
    /* Base styling */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Main container and background */
    .main, .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0d1b2a 100%);
        background-attachment: fixed;
        color: #e0e0e0;
    }
    
    /* Animated stars background with twinkling effect */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #eee, transparent),
            radial-gradient(2px 2px at 60px 70px, #fff, transparent),
            radial-gradient(1px 1px at 50px 50px, #ddd, transparent),
            radial-gradient(1px 1px at 130px 80px, #fff, transparent),
            radial-gradient(2px 2px at 90px 10px, #fff, transparent),
            radial-gradient(1px 1px at 150px 120px, #fff, transparent),
            radial-gradient(2px 2px at 180px 40px, #eee, transparent);
        background-size: 200px 200px;
        animation: stars 20s linear infinite, twinkle 3s ease-in-out infinite;
        opacity: 0.6;
        z-index: 0;
        pointer-events: none;
    }
    
    @keyframes stars {
        from { transform: translateY(0); }
        to { transform: translateY(-200px); }
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 0.9; }
    }
    
    /* Headers with glow effect */
    h1 {
        color: #00d4ff !important;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.8), 0 0 30px rgba(0, 212, 255, 0.5);
        font-size: 2.5rem !important;
        margin-bottom: 1rem !important;
        animation: headerGlow 3s ease-in-out infinite;
    }
    
    @keyframes headerGlow {
        0%, 100% { text-shadow: 0 0 20px rgba(0, 212, 255, 0.8), 0 0 30px rgba(0, 212, 255, 0.5); }
        50% { text-shadow: 0 0 30px rgba(0, 212, 255, 1), 0 0 40px rgba(0, 212, 255, 0.8), 0 0 50px rgba(0, 255, 136, 0.5); }
    }
    
    h2 {
        color: #00ff88 !important;
        text-shadow: 0 0 15px rgba(0, 255, 136, 0.6), 0 0 25px rgba(0, 255, 136, 0.4);
        font-size: 1.8rem !important;
        margin-bottom: 1rem !important;
        padding-bottom: 0.5rem !important;
        border-bottom: 2px solid rgba(0, 255, 136, 0.3);
        animation: subtitleGlow 2.5s ease-in-out infinite;
    }
    
    @keyframes subtitleGlow {
        0%, 100% { text-shadow: 0 0 15px rgba(0, 255, 136, 0.6), 0 0 25px rgba(0, 255, 136, 0.4); }
        50% { text-shadow: 0 0 20px rgba(0, 255, 136, 0.9), 0 0 30px rgba(0, 255, 136, 0.6); }
    }
    
    h3 {
        color: #00d4ff !important;
        font-size: 1.3rem !important;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }
    
    /* Enhanced Buttons with better interactivity */
    .stButton>button {
        background: linear-gradient(135deg, #00d4ff 0%, #0088ff 100%) !important;
        color: #fff !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.5rem !important;
        width: 100%;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.4), 0 0 0 0 rgba(0, 212, 255, 0.5) !important;
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton>button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.6), 0 0 30px rgba(0, 212, 255, 0.4) !important;
        background: linear-gradient(135deg, #00e5ff 0%, #0099ff 100%) !important;
    }
    
    .stButton>button:active {
        transform: translateY(-1px) scale(0.98) !important;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.5) !important;
    }
    
    /* Enhanced Input fields */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background: rgba(10, 14, 39, 0.9) !important;
        border: 2px solid rgba(0, 212, 255, 0.4) !important;
        border-radius: 10px !important;
        color: #e0e0e0 !important;
        padding: 0.85rem 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.5), inset 0 0 10px rgba(0, 212, 255, 0.1) !important;
        background: rgba(10, 14, 39, 1) !important;
        transform: scale(1.02);
    }
    
    .stTextInput>label, .stNumberInput>label {
        color: #00d4ff !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        text-shadow: 0 0 5px rgba(0, 212, 255, 0.3);
    }
    
    /* Enhanced Cards with 3D effect */
    .mission-card {
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.9) 0%, rgba(20, 25, 48, 0.9) 100%);
        border: 2px solid rgba(0, 212, 255, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .mission-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff);
        background-size: 200% 100%;
        transform: scaleX(0);
        transition: transform 0.4s ease;
        animation: gradientShift 3s linear infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }
    
    .mission-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: #00d4ff;
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.4), 0 0 20px rgba(0, 212, 255, 0.2);
        background: linear-gradient(135deg, rgba(26, 31, 58, 1) 0%, rgba(20, 25, 48, 1) 100%);
    }
    
    .mission-card:hover::before {
        transform: scaleX(1);
    }
    
    .experiment-card {
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.7) 0%, rgba(20, 25, 48, 0.7) 100%);
        border-radius: 14px;
        padding: 1.5rem;
        border-left: 4px solid #00d4ff;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3);
    }
    
    .experiment-card:hover {
        transform: translateX(15px) scale(1.02);
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.4), -5px 0 15px rgba(0, 212, 255, 0.2);
        border-left-color: #00ff88;
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.9) 0%, rgba(20, 25, 48, 0.9) 100%);
    }
    
    /* Enhanced Status badges with pulse animation */
    .status-badge {
        padding: 0.4rem 1rem;
        border-radius: 25px;
        font-size: 0.85rem;
        font-weight: 700;
        display: inline-block;
        margin: 0.2rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .status-active {
        background: rgba(0, 255, 136, 0.2);
        color: #00ff88;
        border: 2px solid #00ff88;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
        animation: pulseGreen 2s ease-in-out infinite;
    }
    
    @keyframes pulseGreen {
        0%, 100% { box-shadow: 0 0 10px rgba(0, 255, 136, 0.3); }
        50% { box-shadow: 0 0 20px rgba(0, 255, 136, 0.6), 0 0 30px rgba(0, 255, 136, 0.3); }
    }
    
    .status-done, .status-completed {
        background: rgba(0, 212, 255, 0.2);
        color: #00d4ff;
        border: 2px solid #00d4ff;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
        animation: pulseCyan 2s ease-in-out infinite;
    }
    
    @keyframes pulseCyan {
        0%, 100% { box-shadow: 0 0 10px rgba(0, 212, 255, 0.3); }
        50% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.6), 0 0 30px rgba(0, 212, 255, 0.3); }
    }
    
    .status-pending, .status-planned {
        background: rgba(255, 193, 7, 0.2);
        color: #ffc107;
        border: 2px solid #ffc107;
        box-shadow: 0 0 10px rgba(255, 193, 7, 0.3);
        animation: pulseYellow 2s ease-in-out infinite;
    }
    
    @keyframes pulseYellow {
        0%, 100% { box-shadow: 0 0 10px rgba(255, 193, 7, 0.3); }
        50% { box-shadow: 0 0 20px rgba(255, 193, 7, 0.6), 0 0 30px rgba(255, 193, 7, 0.3); }
    }
    
    .status-badge:hover {
        transform: scale(1.1);
        letter-spacing: 1px;
    }
    
    /* Enhanced Feature cards for home page */
    .feature-card {
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.7) 0%, rgba(20, 25, 48, 0.7) 100%);
        padding: 2.5rem;
        border-radius: 16px;
        border: 2px solid rgba(0, 212, 255, 0.2);
        text-align: center;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .feature-card::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(0, 212, 255, 0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    .feature-card:hover::after {
        opacity: 1;
        animation: ripple 1.5s ease-out;
    }
    
    @keyframes ripple {
        from { transform: scale(0); opacity: 1; }
        to { transform: scale(1); opacity: 0; }
    }
    
    .feature-card:hover {
        transform: translateY(-15px) scale(1.05);
        border-color: #00d4ff;
        box-shadow: 0 20px 50px rgba(0, 212, 255, 0.5), 0 0 30px rgba(0, 212, 255, 0.3);
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.95) 0%, rgba(20, 25, 48, 0.95) 100%);
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        display: inline-block;
        transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }
    
    .feature-card:hover .feature-icon {
        transform: scale(1.2) rotateY(360deg);
    }
    
    /* Enhanced Login card */
    .login-card {
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.95) 0%, rgba(20, 25, 48, 0.95) 100%);
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 10px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(0, 212, 255, 0.2);
        border: 3px solid rgba(0, 212, 255, 0.4);
        max-width: 500px;
        margin: 4rem auto;
        transition: all 0.5s ease;
        position: relative;
        overflow: hidden;
    }
    
    .login-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(0, 212, 255, 0.3), transparent);
        animation: rotate 4s linear infinite;
    }
    
    @keyframes rotate {
        100% { transform: rotate(360deg); }
    }
    
    .login-card:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 60px rgba(0, 0, 0, 0.7), 0 0 50px rgba(0, 212, 255, 0.4);
        border-color: #00d4ff;
    }
    
    .login-icon {
        font-size: 5rem;
        text-align: center;
        margin-bottom: 1rem;
        animation: pulse 2s ease-in-out infinite, float 3s ease-in-out infinite;
        filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.6));
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.15); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* Enhanced Floating planets with better animation */
    .planet {
        position: fixed;
        border-radius: 50%;
        opacity: 0.15;
        animation: float 20s ease-in-out infinite, orbit 30s linear infinite;
        z-index: 0;
        pointer-events: none;
        box-shadow: 0 0 40px rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .planet:hover {
        opacity: 0.25;
        transform: scale(1.1);
    }
    
    .planet-1 {
        width: 180px;
        height: 180px;
        background: radial-gradient(circle at 30% 30%, #ff6b6b, #c92a2a);
        top: 10%;
        right: 10%;
        animation-delay: 0s;
    }
    
    .planet-2 {
        width: 220px;
        height: 220px;
        background: radial-gradient(circle at 30% 30%, #4dabf7, #1864ab);
        bottom: 15%;
        left: 5%;
        animation-delay: 5s;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-30px) rotate(5deg); }
        50% { transform: translateY(-20px) rotate(-5deg); }
        75% { transform: translateY(-40px) rotate(5deg); }
    }
    
    @keyframes orbit {
        0% { transform: rotate(0deg) translateX(10px) rotate(0deg); }
        100% { transform: rotate(360deg) translateX(10px) rotate(-360deg); }
    }
    
    /* Enhanced Mission count badge */
    .mission-count {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.3), rgba(0, 136, 255, 0.3));
        color: #00d4ff;
        padding: 0.4rem 1rem;
        border-radius: 25px;
        font-size: 0.95rem;
        margin-left: 1rem;
        border: 2px solid rgba(0, 212, 255, 0.5);
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
        font-weight: 700;
        display: inline-block;
        animation: countPulse 2s ease-in-out infinite;
    }
    
    @keyframes countPulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 15px rgba(0, 212, 255, 0.3); }
        50% { transform: scale(1.05); box-shadow: 0 0 25px rgba(0, 212, 255, 0.5); }
    }
    
    /* Enhanced DataFrames */
    .stDataFrame {
        background: rgba(26, 31, 58, 0.9) !important;
        border-radius: 12px !important;
        border: 2px solid rgba(0, 212, 255, 0.3) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(135deg, rgba(10, 14, 39, 0.98) 0%, rgba(15, 19, 44, 0.98) 100%) !important;
        border-right: 3px solid #00d4ff !important;
        box-shadow: 5px 0 20px rgba(0, 212, 255, 0.3) !important;
    }
    
    /* Enhanced Info boxes */
    .stInfo, .stSuccess, .stWarning, .stError {
        background: rgba(26, 31, 58, 0.9) !important;
        border-radius: 12px !important;
        border-left: 4px solid !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
    }
    
    .stInfo {
        border-left-color: #00d4ff !important;
        animation: infoPulse 2s ease-in-out infinite;
    }
    
    @keyframes infoPulse {
        0%, 100% { box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); }
        50% { box-shadow: 0 4px 20px rgba(0, 212, 255, 0.3); }
    }
    
    /* Enhanced Metrics */
    .stMetric {
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.9) 0%, rgba(20, 25, 48, 0.9) 100%);
        padding: 1.5rem;
        border-radius: 14px;
        border: 2px solid rgba(0, 212, 255, 0.3);
        transition: all 0.4s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .stMetric:hover {
        transform: translateY(-5px) scale(1.02);
        border-color: #00d4ff;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.4);
    }
    
    .stMetric label {
        color: #00d4ff !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        text-shadow: 0 0 5px rgba(0, 212, 255, 0.3);
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: #00ff88 !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
    }
    
    .stMetric [data-testid="stMetricDelta"] {
        color: #00d4ff !important;
        font-weight: 600 !important;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(10, 14, 39, 0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #00d4ff, #0088ff);
        border-radius: 10px;
        border: 2px solid rgba(10, 14, 39, 0.5);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #00e5ff, #0099ff);
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }
    
    /* Remove Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Add smooth transitions to all elements */
    * {
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# Database helper function
def get_db_connection():
    conn = sqlite3.connect('space_station.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'crew_id' not in st.session_state:
    st.session_state.crew_id = None
if 'crew_name' not in st.session_state:
    st.session_state.crew_name = None
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.crew_id = None
    st.session_state.crew_name = None
    st.session_state.page = 'home'
    st.rerun()

# Login page
def login_page():
    # Add floating planets
    st.markdown("""
    <div class="planet planet-1"></div>
    <div class="planet planet-2"></div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="login-card">
        <div class="login-icon">🔐</div>
        <h2 style="text-align: center; margin-bottom: 0.5rem;">Crew Authentication</h2>
        <p style="text-align: center; color: #b0b0b0; margin-bottom: 2rem;">Enter your credentials to access the command center</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form("login_form"):
            st.markdown("##### 🆔 Crew ID")
            crew_id = st.number_input("Crew ID", min_value=1, step=1, label_visibility="collapsed")
            
            st.markdown("##### 🔑 Password")
            password = st.text_input("Password", type="password", label_visibility="collapsed")
            
            submit = st.form_submit_button("🚀 Launch Access", use_container_width=True)
            
            if submit:
                if crew_id and password:
                    conn = get_db_connection()
                    crew = conn.execute('SELECT * FROM crew WHERE crew_id = ? AND password = ?',
                                      (crew_id, password)).fetchone()
                    conn.close()
                    
                    if crew:
                        st.session_state.logged_in = True
                        st.session_state.crew_id = crew['crew_id']
                        st.session_state.crew_name = crew['name']
                        st.session_state.page = 'missions'
                        st.success(f"✅ Welcome aboard, {crew['name']}!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid Crew ID or Password!")
                else:
                    st.warning("⚠️ Please enter both Crew ID and Password")
        
        st.markdown("---")
        st.info("""
        **Sample Credentials:**
        - **Crew ID:** 1 | **Password:** pass101 | **Name:** Arjun (Commander)
        - **Crew ID:** 2 | **Password:** pass102 | **Name:** Lina (Pilot)
        - **Crew ID:** 4 | **Password:** pass104 | **Name:** Maria (Scientist)
        """)

# Home page
def home_page():
    # Add floating planets
    st.markdown("""
    <div class="planet planet-1"></div>
    <div class="planet planet-2"></div>
    """, unsafe_allow_html=True)
    
    # Hero section
    st.markdown("""
    <div style="text-align: center; padding: 4rem 2rem; margin-bottom: 3rem;">
        <h1 style="font-size: 3.5rem; margin-bottom: 1rem; background: linear-gradient(135deg, #00d4ff 0%, #00ff88 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
            🌌 Welcome to Space Station Command
        </h1>
        <p style="font-size: 1.3rem; color: #b0b0b0; margin-bottom: 2rem;">
            Your gateway to exploring the cosmos and managing interstellar missions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.logged_in:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🚀 Begin Your Journey", use_container_width=True):
                st.session_state.page = 'login'
                st.rerun()
    else:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("📋 View Your Missions", use_container_width=True):
                st.session_state.page = 'missions'
                st.rerun()
    
    st.markdown("---")
    
    # Features section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3>Mission Control</h3>
            <p style="color: #b0b0b0; line-height: 1.6;">Access and manage all space station missions. Track progress, view details, and coordinate with your crew members.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Mission Analytics</h3>
            <p style="color: #b0b0b0; line-height: 1.6;">View detailed analytics and reports on mission progress, experiment outcomes, and crew performance metrics.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔬</div>
            <h3>Research Experiments</h3>
            <p style="color: #b0b0b0; line-height: 1.6;">Explore cutting-edge scientific experiments conducted across various missions. View results and contribute to discoveries.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🛰️</div>
            <h3>Real-time Updates</h3>
            <p style="color: #b0b0b0; line-height: 1.6;">Stay informed with real-time mission updates, status changes, and important communications from mission control.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">👨‍🚀</div>
            <h3>Crew Management</h3>
            <p style="color: #b0b0b0; line-height: 1.6;">Coordinate with fellow astronauts and scientists. Each crew member has specialized roles and assigned missions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🌍</div>
            <h3>Planetary Exploration</h3>
            <p style="color: #b0b0b0; line-height: 1.6;">Participate in missions exploring Mars, Europa, asteroids, and beyond. Push the boundaries of human exploration.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick stats
    conn = get_db_connection()
    total_missions = conn.execute('SELECT COUNT(*) as count FROM mission').fetchone()['count']
    total_experiments = conn.execute('SELECT COUNT(*) as count FROM experiment').fetchone()['count']
    total_crew = conn.execute('SELECT COUNT(*) as count FROM crew').fetchone()['count']
    conn.close()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🚀 Total Missions", total_missions, delta="Active")
    col2.metric("🔬 Experiments", total_experiments, delta="Running")
    col3.metric("👨‍🚀 Crew Members", total_crew, delta="On Station")
    
    st.markdown("---")
    
    # CTA Section
    st.markdown("""
    <div style="text-align: center; margin-top: 4rem; padding: 3rem; background: rgba(0, 212, 255, 0.05); border-radius: 12px; border: 2px solid rgba(0, 212, 255, 0.2);">
        <h2>Ready to Explore the Universe?</h2>
        <p style="color: #b0b0b0; margin-bottom: 2rem;">
            Join our elite crew of astronauts and scientists as we push the boundaries of space exploration.
            Log in to access your mission assignments and contribute to humanity's greatest adventure.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.logged_in:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🔐 Crew Login", use_container_width=True):
                st.session_state.page = 'login'
                st.rerun()

# Missions page
def missions_page():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <h1>🎯 My Mission Control</h1>
        <p style="color: #b0b0b0;">View your assigned missions and tasks</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<p style='color: #00ff88; text-align: center;'>👨‍🚀 Welcome, <strong>{st.session_state.crew_name}</strong> (Crew ID: {st.session_state.crew_id})</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    conn = get_db_connection()
    
    # Get missions assigned to the logged-in crew member
    assigned_missions = conn.execute('''
        SELECT m.*, c.name as commander_name 
        FROM mission m
        LEFT JOIN crew c ON m.crew_id = c.crew_id
        WHERE m.crew_id = ?
        ORDER BY m.launch_date DESC
    ''', (st.session_state.crew_id,)).fetchall()
    
    conn.close()
    
    # Your Missions Section
    st.markdown(f"""<h2>⭐ Your Missions <span class="mission-count">{len(assigned_missions)}</span></h2>""", unsafe_allow_html=True)
    
    if assigned_missions:
        for idx in range(0, len(assigned_missions), 2):
            col1, col2 = st.columns(2)
            
            # First mission in row
            with col1:
                mission = assigned_missions[idx]
                status_class = "status-active" if "Study" in mission['purpose'] else "status-completed" if "Observe" in mission['purpose'] else "status-planned"
                
                st.markdown(f"""
                <div class="mission-card" style="min-height: 200px;">
                    <h3 style="color: #00d4ff; margin-bottom: 0.5rem;">{mission['name']}</h3>
                    <div style="margin-bottom: 1rem;">
                        <span class="status-badge {status_class}">{mission['purpose']}</span>
                    </div>
                    <p style="color: #b0b0b0; margin-bottom: 0.5rem;">📅 {mission['launch_date']}</p>
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">Mission ID: {mission['mission_id']}<br>Commander: {mission['commander_name']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("🔬 View Experiments", key=f"assigned_{mission['mission_id']}", use_container_width=True):
                    st.session_state.selected_mission = mission['mission_id']
                    st.session_state.page = 'experiments'
                    st.rerun()
            
            # Second mission in row (if exists)
            with col2:
                if idx + 1 < len(assigned_missions):
                    mission = assigned_missions[idx + 1]
                    status_class = "status-active" if "Study" in mission['purpose'] else "status-completed" if "Observe" in mission['purpose'] else "status-planned"
                    
                    st.markdown(f"""
                    <div class="mission-card" style="min-height: 200px;">
                        <h3 style="color: #00d4ff; margin-bottom: 0.5rem;">{mission['name']}</h3>
                        <div style="margin-bottom: 1rem;">
                            <span class="status-badge {status_class}">{mission['purpose']}</span>
                        </div>
                        <p style="color: #b0b0b0; margin-bottom: 0.5rem;">📅 {mission['launch_date']}</p>
                        <p style="color: #e0e0e0; margin-bottom: 1rem;">Mission ID: {mission['mission_id']}<br>Commander: {mission['commander_name']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button("🔬 View Experiments", key=f"assigned_{mission['mission_id']}", use_container_width=True):
                        st.session_state.selected_mission = mission['mission_id']
                        st.session_state.page = 'experiments'
                        st.rerun()
    else:
        st.markdown("""
        <div style="text-align: center; padding: 3rem; color: #666; font-size: 1.1rem;">
            <p>🌟 You don't have any assigned missions yet.</p>
        </div>
        """, unsafe_allow_html=True)
    

# All Missions page
def all_missions_page():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <h1>🌌 All Space Station Missions</h1>
        <p style="color: #b0b0b0;">Browse all missions across the space station</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<p style='color: #00ff88; text-align: center;'>👨‍🚀 Welcome, <strong>{st.session_state.crew_name}</strong> (Crew ID: {st.session_state.crew_id})</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    conn = get_db_connection()
    
    # Get all missions
    all_missions = conn.execute('''
        SELECT m.*, c.name as commander_name 
        FROM mission m
        LEFT JOIN crew c ON m.crew_id = c.crew_id
        ORDER BY m.launch_date DESC
    ''').fetchall()
    
    # Get assigned missions for the logged-in crew member
    assigned_missions = conn.execute('''
        SELECT mission_id FROM mission WHERE crew_id = ?
    ''', (st.session_state.crew_id,)).fetchall()
    
    conn.close()
    
    assigned_ids = [m['mission_id'] for m in assigned_missions]
    
    st.markdown(f"""<h2>🚀 All Missions <span class="mission-count">{len(all_missions)}</span></h2>""", unsafe_allow_html=True)
    
    for idx in range(0, len(all_missions), 2):
        col1, col2 = st.columns(2)
        
        # First mission in row
        with col1:
            mission = all_missions[idx]
            status_class = "status-active" if "Study" in mission['purpose'] else "status-completed" if "Observe" in mission['purpose'] else "status-planned"
            is_assigned = mission['mission_id'] in assigned_ids
            
            assigned_badge = '✓ Assigned' if is_assigned else ''
            assigned_style = 'display: block;' if is_assigned else 'display: none;'
            
            st.markdown(f"""
            <div class="mission-card" style="min-height: 200px; position: relative;">
                <div style="position: absolute; top: 0.5rem; right: 0.5rem; background: rgba(0, 255, 136, 0.2); color: #00ff88; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.85rem; font-weight: 600; border: 2px solid #00ff88; {assigned_style}">{assigned_badge}</div>
                <h3 style="color: #00d4ff; margin-bottom: 0.5rem;">{mission['name']}</h3>
                <div style="margin-bottom: 1rem;">
                    <span class="status-badge {status_class}">{mission['purpose']}</span>
                </div>
                <p style="color: #b0b0b0; margin-bottom: 0.5rem;">📅 {mission['launch_date']}</p>
                <p style="color: #e0e0e0; margin-bottom: 1rem;">Mission ID: {mission['mission_id']}<br>Commander: {mission['commander_name']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔬 View Experiments", key=f"all_{mission['mission_id']}", use_container_width=True):
                st.session_state.selected_mission = mission['mission_id']
                st.session_state.page = 'experiments'
                st.rerun()
        
        # Second mission in row (if exists)
        with col2:
            if idx + 1 < len(all_missions):
                mission = all_missions[idx + 1]
                status_class = "status-active" if "Study" in mission['purpose'] else "status-completed" if "Observe" in mission['purpose'] else "status-planned"
                is_assigned = mission['mission_id'] in assigned_ids
                
                assigned_badge = '✓ Assigned' if is_assigned else ''
                assigned_style = 'display: block;' if is_assigned else 'display: none;'
                
                st.markdown(f"""
                <div class="mission-card" style="min-height: 200px; position: relative;">
                    <div style="position: absolute; top: 0.5rem; right: 0.5rem; background: rgba(0, 255, 136, 0.2); color: #00ff88; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.85rem; font-weight: 600; border: 2px solid #00ff88; {assigned_style}">{assigned_badge}</div>
                    <h3 style="color: #00d4ff; margin-bottom: 0.5rem;">{mission['name']}</h3>
                    <div style="margin-bottom: 1rem;">
                        <span class="status-badge {status_class}">{mission['purpose']}</span>
                    </div>
                    <p style="color: #b0b0b0; margin-bottom: 0.5rem;">📅 {mission['launch_date']}</p>
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">Mission ID: {mission['mission_id']}<br>Commander: {mission['commander_name']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("🔬 View Experiments", key=f"all_{mission['mission_id']}", use_container_width=True):
                    st.session_state.selected_mission = mission['mission_id']
                    st.session_state.page = 'experiments'
                    st.rerun()

# Experiments page
def experiments_page():
    if 'selected_mission' not in st.session_state:
        st.session_state.page = 'missions'
        st.rerun()
        return
    
    mission_id = st.session_state.selected_mission
    
    conn = get_db_connection()
    
    # Get mission details
    mission = conn.execute('SELECT * FROM mission WHERE mission_id = ?', (mission_id,)).fetchone()
    
    if not mission:
        st.error("Mission not found")
        conn.close()
        return
    
    # Get experiments for this mission with crew details
    experiments = conn.execute('''
        SELECT e.*, c.name as crew_name 
        FROM experiment e
        LEFT JOIN crew c ON e.crew_id = c.crew_id
        WHERE e.mission_id = ?
        ORDER BY e.title
    ''', (mission_id,)).fetchall()
    
    conn.close()
    
    # Back button
    if st.button("⬅️ Back to Missions"):
        st.session_state.page = 'missions'
        st.rerun()
    
    st.markdown("---")
    
    # Mission info card
    st.markdown(f"""
    <div style="background: rgba(26, 31, 58, 0.8); border-radius: 12px; padding: 2rem; margin-bottom: 2rem; border: 2px solid rgba(0, 212, 255, 0.3);">
        <h1>🔬 Experiments for Mission: {mission['name']}</h1>
        <div style="display: flex; flex-wrap: wrap; gap: 2rem; margin-top: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.5rem; color: #b0b0b0;">
                <strong style="color: #00ff88;">Purpose:</strong> {mission['purpose']}
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem; color: #b0b0b0;">
                <strong style="color: #00ff88;">Launch Date:</strong> {mission['launch_date']}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if experiments:
        st.markdown(f"""
        <h2>🧪 Experiments List <span class="experiments-count mission-count">{len(experiments)}</span></h2>
        """, unsafe_allow_html=True)
        
        # Display each experiment as a card
        for exp in experiments:
            # Determine status class
            status_class = "status-active" if exp['status'] == 'Active' else "status-done" if exp['status'] == 'Done' else "status-pending"
            
            st.markdown(f"""
            <div class="experiment-card">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                    <h3 style="margin: 0;">🧪 {exp['title']}</h3>
                    <span class="status-badge {status_class}">{exp['status']}</span>
                </div>
                <p style="color: #b0b0b0; line-height: 1.6; margin-bottom: 1rem;">
                    <strong style="color: #00d4ff;">Field:</strong> {exp['field']} | 
                    <strong style="color: #00d4ff;">Lead Researcher:</strong> {exp['crew_name']}
                </p>
                <p style="font-size: 0.85rem; color: #666; font-family: 'Courier New', monospace;">
                    Experiment ID: {exp['experiment_id']}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📊 Experiments Summary Table")
        
        # Create a DataFrame for table display
        exp_data = []
        for exp in experiments:
            exp_data.append({
                'ID': exp['experiment_id'],
                'Title': exp['title'],
                'Field': exp['field'],
                'Status': exp['status'],
                'Researcher': exp['crew_name']
            })
        
        df = pd.DataFrame(exp_data)
        
        # Display as styled table
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "ID": st.column_config.NumberColumn("Exp ID", width="small"),
                "Title": st.column_config.TextColumn("Experiment Title", width="medium"),
                "Field": st.column_config.TextColumn("Field", width="medium"),
                "Status": st.column_config.TextColumn("Status", width="small"),
                "Researcher": st.column_config.TextColumn("Lead Researcher", width="medium"),
            }
        )
    else:
        st.markdown("""
        <div style="text-align: center; padding: 3rem; color: #666; font-size: 1.1rem; background: rgba(26, 31, 58, 0.6); border-radius: 12px; border: 2px dashed rgba(0, 212, 255, 0.3);">
            <p>🔬 No experiments found for this mission.</p>
        </div>
        """, unsafe_allow_html=True)

# Main app navigation
def main():
    # Enhanced custom navigation bar with animations
    if st.session_state.logged_in:
        nav_html = f"""
        <nav style="background: linear-gradient(135deg, rgba(10, 14, 39, 0.98) 0%, rgba(15, 19, 44, 0.98) 100%); 
                    padding: 1.2rem 2rem; 
                    box-shadow: 0 6px 30px rgba(0, 200, 255, 0.4), 0 0 20px rgba(0, 255, 136, 0.2); 
                    border-bottom: 3px solid;
                    border-image: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff) 1;
                    position: sticky; 
                    top: 0; 
                    z-index: 10000; 
                    margin: -1rem -1rem 2rem -1rem;
                    backdrop-filter: blur(10px);
                    animation: navSlideDown 0.5s ease-out;">
            <div style="max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="font-size: 2.5rem; animation: logoSpin 3s linear infinite;">🚀</div>
                    <div>
                        <div style="font-size: 1.6rem; font-weight: 800; 
                                    background: linear-gradient(135deg, #00d4ff 0%, #00ff88 100%);
                                    -webkit-background-clip: text;
                                    -webkit-text-fill-color: transparent;
                                    background-clip: text;
                                    text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
                                    letter-spacing: 1px;">
                            Space Station Command
                        </div>
                        <div style="font-size: 0.75rem; color: #00ff88; font-weight: 600; letter-spacing: 2px; text-transform: uppercase;">
                            Mission Control Center
                        </div>
                    </div>
                </div>
                <div style="display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap;">
                    <div style="background: linear-gradient(135deg, rgba(0, 255, 136, 0.2), rgba(0, 212, 255, 0.2));
                                padding: 0.7rem 1.5rem;
                                border-radius: 30px;
                                border: 2px solid rgba(0, 255, 136, 0.4);
                                box-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
                                animation: userBadgePulse 2s ease-in-out infinite;">
                        <span style="color: #00ff88; font-size: 1.2rem; margin-right: 0.5rem;">👨‍🚀</span>
                        <span style="color: #e0e0e0; font-weight: 600; font-size: 1rem;">{st.session_state.crew_name}</span>
                        <span style="color: #00d4ff; margin-left: 0.5rem; font-size: 0.85rem;">ID: {st.session_state.crew_id}</span>
                    </div>
                </div>
            </div>
        </nav>
        <style>
            @keyframes navSlideDown {{
                from {{ transform: translateY(-100%); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
            @keyframes logoSpin {{
                0%, 90% {{ transform: rotate(0deg); }}
                95% {{ transform: rotate(20deg); }}
                100% {{ transform: rotate(0deg); }}
            }}
            @keyframes userBadgePulse {{
                0%, 100% {{ box-shadow: 0 0 20px rgba(0, 255, 136, 0.3); }}
                50% {{ box-shadow: 0 0 30px rgba(0, 255, 136, 0.6), 0 0 40px rgba(0, 212, 255, 0.3); }}
            }}
        </style>
        """
        st.markdown(nav_html, unsafe_allow_html=True)
        
        # Enhanced Navigation buttons with icons
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        with col1:
            if st.button("🏠 Home", use_container_width=True, key="nav_home"):
                st.session_state.page = 'home'
                st.rerun()
        with col2:
            if st.button("🎯 My Missions", use_container_width=True, key="nav_missions"):
                st.session_state.page = 'missions'
                st.rerun()
        with col3:
            if st.button("🌌 All Missions", use_container_width=True, key="nav_all_missions"):
                st.session_state.page = 'all_missions'
                st.rerun()
        with col4:
            st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        with col5:
            if st.button("🚪 Logout", use_container_width=True, key="nav_logout"):
                logout()
    else:
        nav_html = f"""
        <nav style="background: linear-gradient(135deg, rgba(10, 14, 39, 0.98) 0%, rgba(15, 19, 44, 0.98) 100%); 
                    padding: 1.2rem 2rem; 
                    box-shadow: 0 6px 30px rgba(0, 200, 255, 0.4), 0 0 20px rgba(0, 255, 136, 0.2); 
                    border-bottom: 3px solid;
                    border-image: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff) 1;
                    position: sticky; 
                    top: 0; 
                    z-index: 10000; 
                    margin: -1rem -1rem 2rem -1rem;
                    backdrop-filter: blur(10px);
                    animation: navSlideDown 0.5s ease-out;">
            <div style="max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="font-size: 2.5rem; animation: logoSpin 3s linear infinite;">🚀</div>
                    <div>
                        <div style="font-size: 1.6rem; font-weight: 800; 
                                    background: linear-gradient(135deg, #00d4ff 0%, #00ff88 100%);
                                    -webkit-background-clip: text;
                                    -webkit-text-fill-color: transparent;
                                    background-clip: text;
                                    text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
                                    letter-spacing: 1px;">
                            Space Station Command
                        </div>
                        <div style="font-size: 0.75rem; color: #00ff88; font-weight: 600; letter-spacing: 2px; text-transform: uppercase;">
                            Mission Control Center
                        </div>
                    </div>
                </div>
                <div style="color: #00d4ff; font-size: 1.2rem; font-weight: 600; animation: blinkText 2s ease-in-out infinite;">
                    🌌 Exploring the Final Frontier
                </div>
            </div>
        </nav>
        <style>
            @keyframes navSlideDown {{
                from {{ transform: translateY(-100%); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
            @keyframes logoSpin {{
                0%, 90% {{ transform: rotate(0deg); }}
                95% {{ transform: rotate(20deg); }}
                100% {{ transform: rotate(0deg); }}
            }}
            @keyframes blinkText {{
                0%, 100% {{ opacity: 0.7; }}
                50% {{ opacity: 1; text-shadow: 0 0 20px rgba(0, 212, 255, 0.6); }}
            }}
        </style>
        """
        st.markdown(nav_html, unsafe_allow_html=True)
        
        # Navigation buttons for non-logged in users
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        with col1:
            if st.button("🏠 Home", use_container_width=True, key="nav_home_guest"):
                st.session_state.page = 'home'
                st.rerun()
        with col2:
            if st.button("🔐 Login", use_container_width=True, key="nav_login_guest"):
                st.session_state.page = 'login'
                st.rerun()
    
    st.markdown("---")
    
    # Page routing
    if not st.session_state.logged_in and st.session_state.page in ['missions', 'all_missions', 'experiments']:
        st.session_state.page = 'login'
    
    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'login':
        login_page()
    elif st.session_state.page == 'missions':
        missions_page()
    elif st.session_state.page == 'all_missions':
        all_missions_page()
    elif st.session_state.page == 'experiments':
        experiments_page()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <footer style="text-align: center; padding: 2rem; margin-top: 4rem; color: #666; font-size: 0.9rem;">
        <p>🌌 Space Station Command Center | Exploring the Final Frontier | 2026</p>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
