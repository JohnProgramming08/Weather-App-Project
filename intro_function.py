import sqlite3

def sign_up(app):
    username = app.intro_page.username_entry2.get()
    password = app.intro_page.password_entry2.get()
    confirm_password = app.intro_page.confirm_password_entry.get()

    # Connect to the database
    connection = sqlite3.connect("weather_app.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    # Display an error message if the details are invalid
    if user:
        app.show_error("Username already exists")

    elif password != confirm_password:
        app.show_error("Passwords do not match")

    elif len(password) == 0 or len(username) == 0:
        app.show_error("Password and username cannot be empty")

    # If the details are valid, add the user to the database
    else:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        connection.commit()
        app.change_page()
    
    connection.close()