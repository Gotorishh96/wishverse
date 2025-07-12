from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root",
        database="wishverse"
    )

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gallery')
def gallery():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM photos")
    images = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("gallery.html", images=images)

@app.route('/letter')
def letter():
    return render_template("letter.html")

@app.route('/timeline')
def timeline():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM timeline_events ORDER BY event_date ASC")
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("timeline.html", events=events)

if __name__ == '__main__':
    app.run(debug=True)
