import mysql.connector
import os

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ''  # Update with your MySQL password if needed
}

# Read the SQL dump file
sql_file_path = 'space_station.sql'

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    print("Connected to MySQL server successfully!")
    
    # Create database if it doesn't exist
    cursor.execute("DROP DATABASE IF EXISTS space_station")
    cursor.execute("CREATE DATABASE space_station")
    print("Database 'space_station' created successfully!")
    
    # Close connection and reconnect to the new database
    cursor.close()
    conn.close()
    
    # Reconnect with database selected
    db_config['database'] = 'space_station'
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Read and execute SQL file
    print(f"\nImporting data from {sql_file_path}...")
    
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    # Split by semicolons and execute each statement
    statements = sql_content.split(';')
    
    for statement in statements:
        statement = statement.strip()
        if statement and not statement.startswith('--') and not statement.startswith('/*'):
            try:
                cursor.execute(statement)
            except mysql.connector.Error as err:
                # Skip errors from DROP statements and comments
                if 'DROP' not in statement and 'SET' not in statement:
                    print(f"Warning: {err}")
    
    conn.commit()
    
    print("\n✅ Database imported successfully!")
    
    # Display sample data
    print("\n" + "="*60)
    print("SAMPLE LOGIN CREDENTIALS:")
    print("="*60)
    
    cursor.execute("SELECT crew_id, name, role, password FROM crew LIMIT 10")
    crews = cursor.fetchall()
    
    for crew in crews:
        print(f"CrewID: {crew[0]} | Password: {crew[3]} | Name: {crew[1]} | Role: {crew[2]}")
    
    print("="*60)
    
    print("\n" + "="*60)
    print("MISSIONS:")
    print("="*60)
    
    cursor.execute("SELECT mission_id, name, purpose, launch_date FROM mission")
    missions = cursor.fetchall()
    
    for mission in missions:
        print(f"Mission {mission[0]}: {mission[1]} - {mission[2]} (Launch: {mission[3]})")
    
    print("="*60)
    
    cursor.close()
    conn.close()
    
    print("\n🚀 Ready to launch! Run: python app.py")
    
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
except FileNotFoundError:
    print(f"❌ Error: SQL file '{sql_file_path}' not found!")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
