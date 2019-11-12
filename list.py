primes = [] # empty list
for n in range(2,21):
    ans = True
    for i in range(2,n):
        if n % i == 0:
            ans = False
            break

    if ans == True:

        print(primes))
