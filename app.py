from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome.html')
def welcome():
    return render_template('welcome.html')

@app.route('/video.html')
def video():
    room = request.args.get('room')
    return render_template('video.html', room=room)

if __name__ == '__main__':
    app.run(debug=True)
