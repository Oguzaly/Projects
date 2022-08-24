import random
name_length = 32
characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
name =""
for index in range(name_length):
    name  = name + random.choice(characters)
print(name)
