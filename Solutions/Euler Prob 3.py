'''
Project Euler Problem #3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

#Note: Primes are sympy's bitch.

import sympy as sy
print(max(sy.primefactors(600851475143)))