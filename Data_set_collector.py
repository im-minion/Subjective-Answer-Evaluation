from flask import Flask, render_template , request
from firebase import firebase

app = Flask(__name__)
firebasevar = firebase.FirebaseApplication('https://datasetcollector-b1daa.firebaseio.com/')

@app.route('/')
def Base_qstn_paper_set():
    return render_template('first.html')

@app.route('/foo',methods=['POST','GET'])
def foo1():
    if request.method == 'POST':
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']
        fourth = request.form['fourth']
        fifth = request.form['fifth']
        ans = [first,second,third,fourth,fifth]
        result = firebasevar.post('/Users/', data=ans, params={'print': 'pretty'},
                               headers={'X_FANCY_HEADER': 'VERY FANCY'})
        print(result)
    return render_template('submitted.html')
if __name__ == '__main__':
    app.run()
