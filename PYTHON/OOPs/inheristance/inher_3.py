#MULTIPLE INHERITANCE

class A:   # PARENT 1
    VarA= "Welcome to class A"

class B:   # PARENT 2
    VarB= "Welocome to class B"

class C(A, B):  # CHILD CLASS AND INHERIT OF PARENT 1 AND 2, so this is called multiple inheritance 
    VarC = "Welocme to class C"


st1 = C()

print(st1.VarA)
print(st1.VarB)
print(st1.VarC)