n= int(input("enter a n:"))
ans= True
for i in range(2,n):
    if n % i ==0:
        ans = False
        break
print(ans)
