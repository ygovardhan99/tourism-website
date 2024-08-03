from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for locations page
@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/registersuccess')
def registersuccess():
    return render_template('registersuccess.html')

# Route for register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['myname1']
        email = request.form['myemail']
        phone = request.form['myphone']
        age = request.form['myage']
        gender = request.form['mygender']
        departure_date = request.form['departuredate']
        return_date = request.form['returndate']
        travel_destination = request.form.getlist('td')
        package = request.form['locations']

        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (name, email, phone, age, gender, departure_date, return_date, travel_destination, package) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (name, email, phone, age, gender, departure_date, return_date, ', '.join(travel_destination), package))
            conn.commit()
            conn.close()
            flash('Registration successful!', 'success')
            return redirect(url_for('registersuccess'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')

# Route for admin login page

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('admin_login'))
    return render_template('admin_login.html')

# Route for admin dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    return render_template('admin_dashboard.html', users=users)

# Route for admin logout
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    app.run(debug=True)
