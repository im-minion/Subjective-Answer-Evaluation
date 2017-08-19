from flask import Flask, render_template , request
from firebase import firebase

app = Flask(__name__)
firebasevar = firebase.FirebaseApplication('https://datasetcollector-b1daa.firebaseio.com/')

@app.route('/')
def Base_qstn_paper_set():
    return render_template('AuthThings.html')

@app.route('/auth',methods=['POST','GET'])
def auth():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        print(fname," ",lname)
    return render_template('first.html')

@app.route('/foo',methods=['POST','GET'])
def foo():
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

# def auth_with_password(self, email, password):
#     request_ref = 'https://auth.firebase.com/auth/firebase?firebase={0}&email={1}&password={2}'.\
#         format(self.fire_base_name, email, password)
#     request_object = self.requests.get(request_ref)
#     return request_object.json()
if __name__ == '__main__':
    app.run()
