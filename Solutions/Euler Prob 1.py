'''
Project Euler Problem #1:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

a=[0]
b=[0]
c=[0]

s=0
while s < 333:
    s=(s+1)
    t=(s*3)
    a.append(t)

s=0
while s<200:
    s=(s+1)
    t=(s*5)
    b.append(t)

s=0
while s < 66:
    s=(s+1)
    t=(s*15)
    c.append(t)

for x in c:
    a.remove(x)
    b.remove(x)

b.remove(1000)

x=sum(a+b+c)
print(x)