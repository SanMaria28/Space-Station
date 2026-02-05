from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = 'space_mission_secret_key_2026'

# Database helper function
def get_db_connection():
    conn = sqlite3.connect('space_station.db')
    conn.row_factory = sqlite3.Row
    return conn

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'crew_id' not in session:
            flash('Please login to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        crew_id = request.form['crew_id']
        password = request.form['password']
        
        conn = get_db_connection()
        crew = conn.execute('SELECT * FROM crew WHERE crew_id = ? AND password = ?',
                          (crew_id, password)).fetchone()
        conn.close()
        
        if crew:
            session['crew_id'] = crew['crew_id']
            session['crew_name'] = crew['name']
            flash(f'Welcome aboard, {crew["name"]}!', 'success')
            return redirect(url_for('missions'))
        else:
            flash('Invalid CrewID or Password!', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/missions')
@login_required
def missions():
    conn = get_db_connection()
    
    # Get all missions
    all_missions = conn.execute('SELECT * FROM mission ORDER BY launch_date DESC').fetchall()
    
    # Get missions assigned to the logged-in crew member
    assigned_missions = conn.execute('''
        SELECT * FROM mission 
        WHERE crew_id = ?
        ORDER BY launch_date DESC
    ''', (session['crew_id'],)).fetchall()
    
    conn.close()
    
    return render_template('missions.html', 
                         all_missions=all_missions, 
                         assigned_missions=assigned_missions)

@app.route('/experiments/<int:mission_id>')
@login_required
def experiments(mission_id):
    conn = get_db_connection()
    
    # Get mission details
    mission = conn.execute('SELECT * FROM mission WHERE mission_id = ?', (mission_id,)).fetchone()
    
    # Get experiments for this mission with crew details
    experiments = conn.execute('''
        SELECT e.*, c.name as crew_name 
        FROM experiment e
        LEFT JOIN crew c ON e.crew_id = c.crew_id
        WHERE e.mission_id = ?
        ORDER BY e.title
    ''', (mission_id,)).fetchall()
    
    conn.close()
    
    return render_template('experiments.html', 
                         mission=mission, 
                         experiments=experiments)

if __name__ == '__main__':
    app.run(debug=True)
