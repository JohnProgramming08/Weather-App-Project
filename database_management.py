import sqlite3

# Connect to the database
connection = sqlite3.connect("weather_app.db")
cursor = connection.cursor()

# Create the table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
       username TEXT PRIMARY KEY,
       password TEXT)"""
)

# Commit the changes
connection.commit()
connection.close()
