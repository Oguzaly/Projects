import random

class name:
    def __init__(self):
        name_length = 32
        characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        name =""
        for index in range(name_length):
            name  = name + random.choice(characters)

        self.name=name




isim1 = name()
print(isim1.name)
