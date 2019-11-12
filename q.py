print("a*x**2+b*x+c=0")
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))

x=(-b+(b*b-4*a*c)**1/2)/2*a
print ("the value of x:",x)

y=(-b-(b*b-4*a*c)**1/2)/2*a
print ("the value of y:",y)