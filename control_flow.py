'''
sequential    conditional          Iterative/looping
                 if                        while
                 if-else                    for
                 if-elif
                 if-elif-else
transfer statement
1) continue
2) Break
3) pass
'''
x=10
y=20
if x==y:
    print("both are equal")
else:
    print("hello")

# syntax of
a=int(input("enter 1st value"))
# print("1.add\n 2.sub\n 3.div\n 4.multiply")
n=int(input("enter your choice no."))
b=int(input("enter 2nd value"))
if n==1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a*b)
elif n==4:
    print(a/b)
else:
    print("please enter correct no")