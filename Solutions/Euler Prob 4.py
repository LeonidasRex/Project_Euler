'''
Project Euler Problem #4:

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

giant_list = [(i*j) for i in range(100,1000) for j in range(100,1000)]
giant_list.sort()
giant_list = [str(i) for i in giant_list]

for i in giant_list:
    if i == i[::-1]:
       print(i)

