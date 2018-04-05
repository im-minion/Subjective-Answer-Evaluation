# Subjective-Answer-Evaluation

### LOGIC and CONCEPT

IDEA is to evalaute the subjective/descriptive answers from the model answer is provided.
Basically for the first attempt I have ceated a Python Flask App which is hosted at https://pure-woodland-16548.herokuapp.com where student can give there answer.
Currently It has 3 general OOPS related questions. After submiting the data goes to Firebase.
And when the "givVal.py" script is executed it will evaluate and store in Firebase DB the answers of each question based on ML algorithm that I have implemented.

At the core NB classifier is working. With 21 records available in it.

(This dataset is manually written by me after observing some real answersheets evalauted by university Professors.)

(I know its very very very small dataset but still atleast read the complete documentation you'll get to know what I want to say! :) )

(herer is that Dataset https://github.com/im-minion/Subjective-Answer-Evaluation/blob/master/Modules/finaldataset.csv)


For doing this evaluation I have used 3 Parameters 
##### 1.Keywords
##### 2.Grammar
##### 3.Qusetion Specific Things (QST)

The dataset have 4 attributes viz. "keywords", "grammar", "qst"(Qusetion Specific Things) and "class".
"class" is the attribute that ML algo. will predict after providing values of remaining 3 attributes.

So,
the values of "keywords" and "qst" attributes defined as :(1-excellent,2-verygood,3-good,4-ok,5-poor,6-verypoor)

the values of "grammer" attribute defined as: (0-improper,1-proper) and finally

the value of "class" ranges from 1 to 9. 


##### 1.Keywords
Evaluation of Keywords based Cosine Similarity of "student's/user's answer" with "model answer".

Firstly texts (i.e. student's and model answer) converted into vectors. And from these two vectors the Cosine similarity is Calculated.

Now this gives value from 0 to 1. this is converted into numeric form (i.e. 0 to 100). And then keywords will get the value from 1-6


##### 2.Grammar
For this number of grammatical mistakes taken into consideration.

For this API provided by https://textgears.com is used. Thanks for that :) .

##### 3.Qusetion Specific Things (QST)
Fuzzy Logic is used to give the value of qst.

(FuzzyWuzzy libraray from https://github.com/seatgeek/fuzzywuzzy this is used. Thanks for that :) ).



(note: I am begineer in ML and this is my first project in ML. For Any Suggestions please let me know here vaibhavminiyar@gmail.com )

## Usage:
First of all the list of all the required python libraries is as follows:

(You can also fond them at the "requirements.txt" file at the root level of this project)
```
flask
pyrebase
re
math
collections
fuzzywuzzy
sklearn
pandas
numpy
pickle
```
As mentioned previously this project uses Firebase.

So firstly for Firebase configurations,
 ##### 1. Create a firebase project at https://console.firebase.google.com
 
 ##### 2. Create "configurations.py" file at the root level and add the following
```
config = {
    "apiKey": "add your api key",
    "authDomain": "add your domain",
    "databaseURL": "add your DB url",
    "projectId": "add your project id",
    "storageBucket": "add your storage bucket",
    "messagingSenderId": "add your message Id"
}
```

##### 3. Then go to your Firebase Database console click start in realtime databse (select test mode if popo-up comes i.e. database rules must be true for read and write both) and import the json file "temp.json" inside temp folder.

(In temp.json just for an example three model answer and there answers given by 9 users/students are included. So you can evaluate/test them.)

Now, next step is to run the programs
#### 4. So, To give the answers you can run Data_set_collector.py file inside the DataSetCollectoeFlaskApp directory and can give your answers. It is simple flask app which let users to answer the subjective questions.

(Also for evaluating for your own question change the model answer in Firebase DB and the question in flask app and store them in DB as per requirements and test)

#### 5. The main algorithm is in "givVal.py" file inside Modules directory.
Run that file and you will have the answers evaluated by the algorithm inside the DB and it will also print them in the terminal.

:)

for any issues drop an email - vaibhavminiyar@gmail.com
