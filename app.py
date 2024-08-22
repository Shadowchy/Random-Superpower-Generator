from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'powers.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    conn = get_db()
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS powers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS saved_powers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            power_id INTEGER,
            FOREIGN KEY (power_id) REFERENCES powers (id)
        )''')
    conn.close()

@app.route('/')
def home():
    conn = get_db()
    power = conn.execute('SELECT * FROM powers ORDER BY RANDOM() LIMIT 1').fetchone()
    saved_powers = conn.execute('''SELECT p.*
                                  FROM saved_powers sp
                                  JOIN powers p ON sp.power_id = p.id''').fetchall()
    conn.close()
    return render_template('index.html', power=power, saved_powers=saved_powers)

@app.route('/get_power', methods=['POST'])
def get_power():
    conn = get_db()
    power = conn.execute('SELECT * FROM powers ORDER BY RANDOM() LIMIT 1').fetchone()
    saved_powers = conn.execute('''SELECT p.*
                                  FROM saved_powers sp
                                  JOIN powers p ON sp.power_id = p.id''').fetchall()
    conn.close()
    return render_template('index.html', power=power, saved_powers=saved_powers)

@app.route('/save_power', methods=['POST'])
def save_power():
    power_id = request.form['power_id']
    conn = get_db()
    with conn:
        conn.execute('INSERT OR IGNORE INTO saved_powers (power_id) VALUES (?)', (power_id,))
    conn.close()
    return redirect(url_for('home'))

@app.route('/delete_power/<int:power_id>', methods=['POST'])
def delete_power(power_id):
    conn = get_db()
    with conn:
        conn.execute('DELETE FROM saved_powers WHERE power_id = ?', (power_id,))
    conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    initialize_db()  # Initialize the database when the app starts
    app.run(debug=True)
