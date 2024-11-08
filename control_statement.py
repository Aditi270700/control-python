# Range:
# syntax :- range(start, stop, step(direction))
# range (stop)
# range (start,stop)
# range (start,stop,step/direction)
#  x = (2,4,6,8,10)
x1 = range(2,11,2)
x= range(1,10,2)
print (x)
print(list(x))
print(x1)
print(list(x1))
v = range(10)
v1 = range(5,10)
v2 = range(5,10,-5)
print(list(v))
print(list(v1))
print(list(v2))
a=[-3,-2,-1,0,1,2,3]
a = range(-3,4,1)
print(list(a))

b=[2]
b=range(2,3)
print(list(b))

# slicing
my_str = 'aditi'
print(my_str[0:5][0:4][0:2])