# A class method is bound to the class & receives the class as an implicit first agrument.
# note-- static method can't access or modify class state & generally for utility. 
 

class person:
    position = "RPA"
    def changePosition(self, position):
        self.__class__.position = "SDE"

    @classmethod
    def changeName(cls, name):
       cls.name = name 

p1 = person()
p1.changePosition("SDE")
print(person.position)
p1.changeName("Sneha")
print(person.name)