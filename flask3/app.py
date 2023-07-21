from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/page2/<int:score>')
def success(score):
    out_put = ''
    if score >= 50:
        out_put = 'Pass'
    else:
        out_put = 'Fail'
    return render_template('result.html', content_type={'score': score, 'out_put': out_put})

@app.route('/page1', methods=['POST', 'GET'])
def submit():
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