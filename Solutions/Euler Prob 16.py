'''
Project Euler Problem #16:

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

#Ripped and hacked from Solution #8, easy day.

data=str(2**1000)

sum=0
for i in range(len(data)):
    for j in range(i,i+1):
        sum += int(data[j])

print(sum)