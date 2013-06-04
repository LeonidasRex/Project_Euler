'''
Project Euler Problem #10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import sympy as sy

prime_list=[i for i in sy.sieve.primerange(1,2000000)]
print(sum(prime_list))