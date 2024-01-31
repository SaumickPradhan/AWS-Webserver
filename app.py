from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask import send_file

app = Flask(__name__)

# SQLite database initialization
# conn = sqlite3.connect('database.db')

app.config['DATABASE'] = '/var/www/html/flaskapp/database.db'
conn = sqlite3.connect(app.config['DATABASE'])
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )
''')
conn.commit()
conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # conn = sqlite3.connect('database.db')
        # app.config['DATABASE'] = '/var/www/html/flaskapp/database.db'
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user and user[2] == password:
            # User exists, display user_info
            return redirect(url_for('user_info', user=user[3:]))
        else:
            # User does not exist, add to the database
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('get_user_info', username=username))

    return render_template('login.html')



@app.route('/user_info<user>', methods=['GET', 'POST'])
def user_info(user):
    user = tuple(map(str, [element.strip(" '()") for element in user.split(',')]))
    with open("/var/www/html/flaskapp/Limerick.txt", 'r') as file:
        content = file.read()
        words_count = len(content.split())

    return render_template('user_info.html', user_info=user, words_count=words_count, download_file=send_file('/var/www/html/flaskapp/Limerick.txt', as_attachment=True))


@app.route('/download_limerick')
def download_limerick():
    # Provide the correct path to your Limerick.txt file
    file_path = '/var/www/html/flaskapp/Limerick.txt'
    return send_file(file_path, as_attachment=True)


@app.route('/get_user_info/<username>', methods=['GET', 'POST'])
def get_user_info(username):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        # conn = sqlite3.connect('database.db')
        # app.config['DATABASE'] = '/var/www/html/flaskapp/database.db'
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()

        # Update user_info
        cursor.execute('''
            UPDATE users
            SET first_name = ?, last_name = ?, email = ?
            WHERE username = ?
        ''', (first_name, last_name, email, username))

        conn.commit()
        conn.close()

        return render_template('get_user_info.html', user_info=(first_name, last_name, email))

    return render_template('get_user_info.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
