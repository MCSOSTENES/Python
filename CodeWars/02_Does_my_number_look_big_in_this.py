""" 6 Kyu
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
"""
def narcissistic1( value ):
    str = "{}".format(value)
    exp = len(str)
    for i in range(0,exp):
        value -= int(str[i])**exp
    return value == 0

#Melhor resposta 
def narcissistic(value):
    #               soma dos valores de cada casa de value
    return value == sum(int(x) ** len(str(value)) for x in str(value))

print(narcissistic(7))   #, True, '7 is narcissistic');
print(narcissistic(371))   #, True, '371 is narcissistic');print
print(narcissistic(122))   #, False, '122 is not narcissistic')
print(narcissistic(4887))   #, False, '4887 is not narcissistic')