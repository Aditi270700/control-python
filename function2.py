def show(**kwargs):
    print (kwargs)
    for i,j in kwargs.items():
        print(i,"=",j)

show (name='Aditi',age=24, qualification='bsc')