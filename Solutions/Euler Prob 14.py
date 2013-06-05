'''
Project Euler Problem #14:

The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''


def rules(n):
    if n%2 == 0:
        b=n//2
    if n%2 != 0:
        b=(3*n)+1
    return(b)

def sequence(n):
    l=[n]
    i=0
    while l[i] != 1:
        l.append(rules(l[i]))
        i+=1
    return(l)

'''
The following code needs to be optimized when I'm better at programming :(
It takes ~90 seconds but it can be knocked down to seconds or less if I get
rid of the global list that's eating memory for no reason. So dear future me:
Compare term-by-term to see which is greater, rather than holding all numbers in list [ll]
'''
ll=[]
for i in range(1,10**6):
    l=sequence(i)
    ll.append((len(l),i))

print(max((ll)))