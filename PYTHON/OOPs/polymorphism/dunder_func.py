# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def shownumber(self):
        print (self.real,"i +", self.img,"j")
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal, newImg)

num1 = complex(3,6)
num1.shownumber()
num2 = complex(9,4)
num2.shownumber()
num3 = num1 - num2
num3.shownumber()
        