from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Proste bazy danych użytkowników i administratorów (na potrzeby przykładu)
users = {
    'user': {'password': 'userpassword'},
    'admin': {'password': 'adminpassword'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        if password == users[username]['password']:
            if username == 'admin':
                return redirect(url_for('admin_panel'))
            else:
                return redirect(url_for('welcome'))
    
    return redirect(url_for('index'))  # Przekierowanie z powrotem do strony logowania w przypadku niepowodzenia

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/admin')
def admin_panel():
    return render_template('admin.html')

@app.route('/video.html')
def video():
    room = request.args.get('room')
    return render_template('video.html', room=room)

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
