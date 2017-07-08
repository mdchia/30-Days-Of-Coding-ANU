# Implements Rabin-Miller Strong Pseudoprime Test
def is_prime(n):
    #See OEIS A014233
    #Expected to work only up to 10^9 (< 3,215,031,751)
    #checks=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    checks=[2, 3, 5, 7, 11]
    #checks=[2]
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0: #even numbers
        return False
    d=n-1
    s=0
    # Define n as ((2 ** s)*d)-1 with s as odd
    while d % 2 == 0:
        s = s + 1
        d = d // 2
    #print("d:{}, s={}".format(d,s))
    for a in checks:
        if a>=n:
            break
        # a^(d) = 1 (mod n)
        x = pow(a, d, n)
        if x==1 or x==n-1:
            continue
        for j in range(s-1):
            # a^(2^(j) * d) = -1 (mod n)
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Prime generator from https://stackoverflow.com/a/43433272
import math
def primeNr(interval):
    primes=[]
    #if interval itself should be included, then change this to range(2, interval + 1)
    for i in range(2, interval):
        percent=(i/interval)*100
        print('     '+str(int(percent))+"%: "+str(i), end="\r")
        isPrime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes

# Excessively fancy testing function :p
import sys
def primeTest(n):
    print("Preparing primes ...")
    test1=primeNr(n)
    print("Checking test function ...")
    for i in range(n):
        #print(' '+str(i)+" of "+str(len(test1)), end="\r")
        percent=(i/n)*100
        print('     '+str(int(percent))+"%: "+str(i), end="\r")
        #m=probably_prime(i,4)
        m=is_prime(i)
        if not m and i in test1:
            print("False negative" + str(i))
        if m and i not in test1:
            print("False positive" + str(i))
    print("Done!                ")
