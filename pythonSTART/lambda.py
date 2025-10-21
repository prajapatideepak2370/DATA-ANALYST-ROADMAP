double  = lambda x: x*3
cube = lambda x: x*x*x
print(double(5))
print(cube(3))

#Now Create a function and pass the lambda function as an argument
def myfunc(func, num):
    return 6 + func(num)
print(myfunc(cube, 4))

avg = lambda x, y, z: (x + y + z)/3
print(avg(45,34,10))