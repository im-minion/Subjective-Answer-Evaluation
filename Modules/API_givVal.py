import math
import nav_test
import requests
from fuzzywuzzy import fuzz
import Modules.cosine_similarity as keywordVal

def myFun(model_answer, answer, out_of):
    # KEYWORDS =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TODO : Enhance this thing
    if (len(answer.split())) <= 5:
        return 0

    k = keywordVal.givKeywordsValue(model_answer, answer)

    # GRAMMAR =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=JmcxHCCPZ7jfXLF6")
    no_of_errors = len(req.json()['errors'])

    if no_of_errors > 5 or k == 6:
        g = 0
    else:
        g = 1

    # QST =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    q = math.ceil(fuzz.token_set_ratio(model_answer, answer) * 6 / 100)

    print("Keywords : ", k)
    print("Grammar  : ", g)
    print("QST      : ", q)

    predicted = nav_test.predict(k, g, q)
    result = predicted * out_of / 10
    return result[0]


res = myFun(
    "Encapsulation is an object-oriented programming concept that binds together the data and functions that manipulate the data, and that keeps both safe from outside interference and misuse.Data encapsulation led to the important OOP concept of data hiding. If a class does not allow calling code to access internal object data and permits access through methods only, this is a strong form of abstraction or information hiding known as encapsulation. Data encapsulation is a mechanism of bundling the data, and the functions that use them and data abstraction is a mechanism of exposing only the interfaces and hiding the implementation details from the user. Abstraction and encapsulation are complementary concepts: abstraction focuses on the observable behavior of an object. encapsulation focuses upon the implementation that gives rise to this behavior. encapsulation is most often achieved through information hiding, which is the process of hiding all of the secrets of object that do not contribute to its essential characteristics.  Encapsulation is the process of combining data and functions into a single unit called class. In Encapsulation, the data is not accessed directly; it is accessed through the functions present inside the class. In simpler words, attributes of the class are kept private and public getter and setter methods are provided to manipulate these attributes. Thus, encapsulation makes the concept of data hiding possible Abstraction is a process where you show only “relevant” data and “hide” unnecessary details of an object from the user.",
    "It is object oreinted concept related to the data hiding. Abstraction of the program is the encapsulation. It shows the relvant data. It is the mechanism of binding the data, and the function that use them.",
    5)

print("Marks out of 5 ")
print(res)