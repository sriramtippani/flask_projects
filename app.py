from flask import Flask


app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to flask class'

@app.route('/page2')
def metheod_Info():
    return 'Practice makes man perfect'

if __name__ == '__main__':
    app.run(debug=True)