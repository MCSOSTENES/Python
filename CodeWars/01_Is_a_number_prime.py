""" 6Kyu
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ). 
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.

"""

def is_prime1(num):
    if num < 2 or (num**(1/2)).is_integer():
        return False
    if num <10:
        for div in range(2,num):
            if num%div == 0 and num != div:
                return False
    for div in range(2,int(num**(1/2))):
        if num%div == 0: 
            return False
    return True

# melhor solucao ao meu ver
def is_prime(n):
    #se n<1 retorna falso / a funcao all() retorna true se todos os n%i forem diferentes de 0 (false)
    return n>1 and all(n%i for i in range(2, int(n**.5+1)))

print(is_prime(617969881))   #,  False, "0  is not prime")
#print(is_prime(1))   #,  False, "1  is not prime")
#print(is_prime(2))   #,  True, "2  is prime")
#print(is_prime(73))   #, True, "73 is prime")
#print(is_prime(75))   #, False, "75 is not prime")
#print(is_prime(-1))   #, False, "-1 is not prime")
