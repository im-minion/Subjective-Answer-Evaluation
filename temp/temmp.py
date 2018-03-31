from fuzzywuzzy import fuzz

text1 = "Encapsulation is an object-oriented programming concept that binds together the data and functions that manipulate the data, and that keeps both safe from outside interference and misuse." \
        "Data encapsulation led to the important OOP concept of data hiding." \
        "If a class does not allow calling code to access internal object data and permits access through methods only, this is a strong form of abstraction or information hiding known as encapsulation." \
        " Data encapsulation is a mechanism of bundling the data, and the functions that use them and data abstraction is a mechanism of exposing only the interfaces and hiding the implementation details from the user." \
        "Abstraction and encapsulation are complementary concepts: abstraction focuses on the observable behavior of an object. encapsulation focuses upon the implementation that gives rise to this behavior." \
        " encapsulation is most often achieved through information hiding, which is the process of hiding all of the secrets of object that do not contribute to its essential characteristics." \
        " Encapsulation is the process of combining data and functions into a single unit called class." \
        " In Encapsulation, the data is not accessed directly; it is accessed through the functions present inside the class." \
        " In simpler words, attributes of the class are kept private and public getter and setter methods are" \
        " provided to manipulate these attributes." \
        " Thus, encapsulation makes the concept of data hiding possible"

text2 = "It is object oreinted concept related to the data hiding. " \
        "Abstraction of the program is the encapsulation. It shows the relvant data. " \
        "It is the mechanism of binding the data, and the function that use them."

print(fuzz.ratio(text1,text2))