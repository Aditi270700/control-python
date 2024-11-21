'''
x=10
def show():
    global y
    y=20       
    print(x)
    print(y)
show()
print(x)
print(y)
'''
x=20
def show():
    x=50
    print(x)
    print(globals()['x'])
show()
# globals is used to override value