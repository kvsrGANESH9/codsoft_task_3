#Password generator
import random
l=int(input('Enter the length required to generate a password: '))
password= ' '
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='1234567890'
sp='!@#$%^&*()_{}""<>'
string=chars+digits+sp
for i in range(l):
    password+=random.choice(string)
print('THe generated password is: ',password)