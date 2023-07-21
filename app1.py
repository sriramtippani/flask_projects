from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def content():
    return 'Hi I am THeir with flask'

@app.route('/page1/<int:score>')
def success(score):
    return 'The person is passed = ' + str(score)

@app.route('/page2/<int:score>')
def fail(score):
    return 'The person is failed = ' + str(score)

@app.route('/page3/<int:marks>')
def result(marks):
    data = ''
    if marks < 50:
        data = 'fail'
    else:
        data = 'success'
    # return data
    return redirect(url_for(data, score=marks))

if __name__=='__main__':
    app.run(debug=True)