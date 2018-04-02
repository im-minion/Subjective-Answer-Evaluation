from flask import Flask, render_template, request
# from firebase import firebase
import configurations
import pyrebase

app = Flask(__name__)
email = "null"

firebsevar = pyrebase.initialize_app(config=configurations.config)
db = firebsevar.database()


# firebasevar = firebase.FirebaseApplication('https://datasetcollector-b1daa.firebaseio.com/')
# firebase_apikey = "AIzaSyDmbVrxMd2l1Pq18zTvquLUlgBCIPErqqY"

@app.route('/')
def Base_qstn_paper_set():
    return render_template('first.html')


# @app.route('/authSignUp', methods=['POST', 'GET'])
# def authSignUp():
#     if request.method == 'POST':
#         email = request.form['emailId']
#         password = request.form['password']
#         # print(email, " ", password)
#         authvar = firebsevar.auth()
#         authvar.create_user_with_email_and_password(email, password)
#         if authvar.current_user == "None":
#             return render_template('<html><head><title>Error</title></head><body><h1>error</h1></body></html>')
#         else:
#             db.child("users").child("email").push(email)
#             return render_template('first.html')
# temp = register(email, password)
# if temp == "success":
#     return render_template('first.html')
# else:
#     return render_template('AuthThings.html')
#
# @app.route('/authSignIn', methods=['POST', 'GET'])
# def authSignIn():
#     if request.method == 'POST':
#         email = request.form['emailId_in']
#         password = request.form['password_in']
#         # print(email, " ", password)
#
#         # temp = signin(email, password)
#         try :
#             authvar = firebsevar.auth()
#             user = authvar.sign_in_with_email_and_password(email, password)
#             authvar = firebsevar.auth()
#             # print(authvar.current_user)
#             return render_template('first.html')
#         except requests.exceptions.HTTPError as e:
#             # print(e.__doc__)
#             return render_template('<html><head><title>Error</title></head><body><h1>error</h1></body></html>')
# if temp == "success":
#     return render_template('first.html')
# else:
#     return render_template('AuthThings.html')

@app.route('/foo', methods=['POST', 'GET'])
def foo():
    if request.method == 'POST':
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']

        email = request.form['emailID']

        ans = {"a1": first, "a2": second, "a3": third, "email": email}

        result = db.child("/answers").push(ans)

        # authvar = firebsevar.auth()
        # print(authvar.current_user)
        # result = firebasevar.post('/answers/', data=ans, params={'print': 'pretty'},
        #                           headers={'X_FANCY_HEADER': 'VERY FANCY'})
        # print(result)
    return render_template('first.html')


#
# def register(email, password):
#     my_data = dict()
#     my_data["email"] = email
#     my_data["password"] = password
#     my_data["returnSecureToken"] = True
#     json_data = json.dumps(my_data).encode()
#     headers = {"Content-Type": "application/json"}
#     request = urllib.request.Request(
#         "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + firebase_apikey,
#         data=json_data, headers=headers)
#     try:
#         loader = urllib.request.urlopen(request)
#
#     except urllib.error.URLError as e:
#         message = json.loads(e.read())
#         print(message["error"]["message"])
#         return (message["error"]["message"])
#     else:
#         print(loader.read())
#         # userdata = [email,password]
#         # firebasevar.post('/users/', data=userdata, params={'print': 'pretty'},
#         #                           headers={'X_FANCY_HEADER': 'VERY FANCY'})
#         return "success"
#
# def signin(email, password):
#     my_data = dict()
#     my_data["email"] = email
#     my_data["password"] = password
#     my_data["returnSecureToken"] = True
#     json_data = json.dumps(my_data).encode()
#     headers = {"Content-Type": "application/json"}
#     request = urllib.request.Request(
#         "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + firebase_apikey,
#         data=json_data, headers=headers)
#     try:
#         loader = urllib.request.urlopen(request)
#     except urllib.error.URLError as e:
#         message = json.loads(e.read())
#         print(message["error"]["message"])
#         return (message["error"]["message"])
#     else:
#         print(loader.read())
#         return "success"

if __name__ == '__main__':
    app.run()
