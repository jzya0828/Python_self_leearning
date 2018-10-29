
#------tips1：Modularing Codes----
#write gcd function in py1.py
def gcd(n1,n2):
    gcd = 1
    k = 2

    while k <= n1 and k <= n2:
        if n1 % k==0 and n2 % k==0:
            gcd = k
        k += 1

    return gcd

#write py2.py and use 'from xxx import xxx to use gcd function
from GCDfunction import gcd

n1 = eval(input('input n1: '))
n2 = eval(input('input n2: '))

print('the greatest common divisor for ',n1,' and ',n2,'is',gcd(n1,n2))