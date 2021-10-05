#Question No.1

def numb():
    numb = []
    for i in  range(2000,3201):
        if (i % 7 == 0) and (i % 5 == 0):
            numb.append(str(i))
    print("," .join(numb))
numb()

# Question no. 2
def name():
    name1 = input("enter your first name  ")
    name2 = input("enter your second name  ")
    print(name2 + " " + name1)
name()

#Question no. 3

def sphere():
    import math
    pi = math.pi
    r = float(12/2)
    v = float(4/3 * pi * r*r*r)
    print ("volume of shere", v)
sphere()



