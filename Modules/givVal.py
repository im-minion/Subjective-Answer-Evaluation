from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import nav_test
import pyrebase
import math
import json
import requests
import re

'''
e = 1
vg = 2
g = 3
o = 4
p = 5
vp = 6

Grammar:
y = 1
n = 0
'''


def givVal(model_answer, keywords, answer, out_of):
	# KEYWORDS =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# TODO : Enhacnce this thing
	count = 0
	for i in range(len(keywords)):
		if keywords[i] in answer:
			# print (keywords[i])
			count = count + 1
	k = 0
	if(count==len(keywords)):
		k = 1
	elif( count== (len(keywords)-1)):
		k = 2
	elif (count==(len(keywords)-2)):
		k = 3
	elif (count==(len(keywords)-3)):
		k = 4
	elif (count==(len(keywords)-4)):
		k = 5
	elif (count==(len(keywords)-5)):
		k = 6

	# GRAMMAR =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	req = requests.get("https://api.textgears.com/check.php?text="+answer+"&key=JmcxHCCPZ7jfXLF6")
	no_of_errors = len(req.json()['errors'] )

	if no_of_errors > 5:
		g = 0
	else:
		g = 1

	# QST =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	print("fuzz1 ratio: ",fuzz.ratio(model_answer,answer))
	q = math.ceil(fuzz.token_set_ratio(model_answer,answer) * 6 / 100)

	print("Keywords : ",k)
	print("Grammar : ",g)
	print("Qusestion Specific Things : ",q)

	predicted = nav_test.predict(k,g,q)
	# Mathematical model->
	# predicted / 10
	# what?	/ out_of
	result = predicted * out_of / 10
	return result[0]




# model_answer = 'Encapsulation is an object-oriented programming concept that binds together the data and functions that manipulate the data, and that keeps both safe from outside interference and misuse.Data encapsulation led to the important OOP concept of data hiding. If a class does not allow calling code to access internal object data and permits access through methods only, this is a strong form of abstraction or information hiding known as encapsulation. Data encapsulation is a mechanism of bundling the data, and the functions that use them and data abstraction is a mechanism of exposing only the interfaces and hiding the implementation details from the user. Abstraction and encapsulation are complementary concepts: abstraction focuses on the observable behavior of an object. encapsulation focuses upon the implementation that gives rise to this behavior. encapsulation is most often achieved through information hiding, which is the process of hiding all of the secrets of object that do not contribute to its essential characteristics.  Encapsulation is the process of combining data and functions into a single unit called class. In Encapsulation, the data is not accessed directly; it is accessed through the functions present inside the class. In simpler words, attributes of the class are kept private and public getter and setter methods are provided to manipulate these attributes. Thus, encapsulation makes the concept of data hiding possible Abstraction is a process where you show only “relevant” data and “hide” unnecessary details of an object from the user.'

# answer1 = 'It is object oreinted concept related to the data hiding. Abstraction of the program is the encapsulation. It shows the relvant data. It is the mechanism of binding the data, and the function that use them.'

# answer2 = 'Encapsulation is hiding data. It can be visualised as an Abstract view of the program. '

# keywords = ['binds', 'together', 'relevant data', 'data hiding', 'data hiding', 'abstraction', 'combining data']

config = {
    "apiKey": "AIzaSyDmbVrxMd2l1Pq18zTvquLUlgBCIPErqqY",
    "authDomain": "datasetcollector-b1daa.firebaseapp.com",
    "databaseURL": "https://datasetcollector-b1daa.firebaseio.com",
    "projectId": "datasetcollector-b1daa",
    "storageBucket": "datasetcollector-b1daa.appspot.com",
    "messagingSenderId": "532795544470"
}

firebsevar = pyrebase.initialize_app(config=config)
db = firebsevar.database()

model_answer1 = db.child("model_answers").get().val()[1]['answer']
out_of1 = db.child("model_answers").get().val()[1]['out_of']
keywords1 = db.child("model_answers").get().val()[1]['keywords']
keywords1 = re.findall(r"[a-zA-Z]+",keywords1)

model_answer2 = db.child("model_answers").get().val()[2]['answer']
out_of2 = db.child("model_answers").get().val()[2]['out_of']
keywords2 = db.child("model_answers").get().val()[2]['keywords']
keywords2 = re.findall(r"[a-zA-Z]+",keywords2)

model_answer3 = db.child("model_answers").get().val()[3]['answer']
out_of3 = db.child("model_answers").get().val()[3]['out_of']
keywords3 = db.child("model_answers").get().val()[3]['keywords']
keywords3 = re.findall(r"[a-zA-Z]+",keywords3)


# print(model_answer1)
# print(model_answer2)
# print(model_answer3)

# print(keywords1)
# print(keywords2)
# print(keywords3)



all_answers = db.child("answers").get()

for each_users_answers in all_answers.each():
	# For the first answer ->
	answer = each_users_answers.val()['1']
	result = givVal(model_answer1, keywords1, answer, out_of1)
	db.child("answers").child(each_users_answers.key()).update({"result1":result})

	# For the Second answer ->
	answer = each_users_answers.val()['2']
	result = givVal(model_answer2, keywords2, answer, out_of2)
	db.child("answers").child(each_users_answers.key()).update({"result2":result})

	# For the third answer ->
	answer = each_users_answers.val()['3']
	result = givVal(model_answer3, keywords3, answer, out_of3)
	db.child("answers").child(each_users_answers.key()).update({"result3":result})




# out_of = 5
# result = givVal(model_answer, keywords, answer1, out_of)
# print("Final Result : ",result)

# print("fuzzz2 : ",fuzz.token_set_ratio(model_answer,answer2))


# qst1 = answer1.split('Example' or 'eg' or 'example')

# print(qst1[1])