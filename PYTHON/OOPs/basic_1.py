#CLASS & OBJECT 

#Creating a Class
class student:
    name = "Deepak"

#Creating Object(Instance)
s1 = student()
print(s1.name)  #Accessing the class attribute using the object

#--------------------------------------------------------------------------------------------------------------------
#making another Class and Object 
class car:
    color = "Black"
    brand = "AUDI"

car1 = car()
print(car1.color)
print(car1.brand)