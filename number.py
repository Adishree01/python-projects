a= int(input("enter first number"))
b= int(input("enter second number"))
c= int(input("enter third number"))
if (a > b) and (a > c):
    number= a
    print('the greatest number is '+str(a))
elif (b >= a) and (b >= c):
    number= b
    print('the greatest number is '+str(b))
else:
    number= c
    print("the greatest number is"+str(c))


