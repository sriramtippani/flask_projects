from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def welcomepage():
    return render_template('index.html')

@app.route('/page2/<int:score>')
def success(score):
    re = ''
    if score >= 50:
        re = 'Pass'
    else:
        re = 'Fail'
    return render_template('result.html', output=re)

@app.route('/page1', methods=['POST', 'GET'])
def submitpage():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['data_science'])

        total_score = (science + maths + c + datascience) / 4

    return redirect(url_for('success', score=total_score))


if __name__ == '__main__':
    app.run(debug=True)