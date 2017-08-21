import json
import urllib

from flask import Flask, render_template , request
from firebase import firebase

app = Flask(__name__)
firebasevar = firebase.FirebaseApplication('https://datasetcollector-b1daa.firebaseio.com/')
firebase_apikey = "AIzaSyDmbVrxMd2l1Pq18zTvquLUlgBCIPErqqY"
@app.route('/')
def Base_qstn_paper_set():
    return render_template('AuthThings.html')

@app.route('/authSignUp',methods=['POST','GET'])
def authSignUp():
    if request.method == 'POST':
        email = request.form['emailId']
        password = request.form['password']
        print(email," ",password)
        register(email, password)
        # auth_with_password(fName,lName)
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
#     print(request_object)
#     return request_object.json()

def register(email, password):

    my_data = dict()
    my_data["email"] = email
    my_data["password"] = password
    my_data["returnSecureToken"] = True

    print("a")

    json_data = json.dumps(my_data).encode()
    headers = {"Content-Type": "application/json"}
    request = urllib.request.Request("https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key="+firebase_apikey, data=json_data, headers=headers)

    print("b")

    try:
        loader = urllib.request.urlopen(request)
        print("c")

    except urllib.error.URLError as e:
        message = json.loads(e.read())
        print(message["error"]["message"])
    else:
        print(loader.read())
if __name__ == '__main__':
    app.run()
