# class Fruit:
#     def __init__(self):
#         self.name="Apple"   #Attribute
#         self.colour="Red"   #Attribute
#
#
#
# my_fruit = Fruit()
#
# print(my_fruit.colour)
# print(my_fruit.name)
#
# my_fruit.colour ='green'
# my_fruit.name ='kiwi'
#
# print(my_fruit.name)
# print(my_fruit.colour)

####################################
#Yukarıdaki örnek çok sınırlı bir örnek o yüzden aşağıdaki gibi yapmak en güzeli
#####################################


class Fruit:
    def __init__(self,name,clr):
        self.name=name   #Attribute
        self.colour=clr   #Attribute


apple = Fruit("apple","red")
print(apple)
print(apple.name)
print(apple.colour)


#####################################3
#peki buna nasıl method ekleriz
#################################

class Fruit:
    def __init__(self,name,clr):        #init de details da method aslında self kollandığımızda init de tanıttığımız objeye details kısmında ulaşabiliyoruz
        self.name=name
        self.colour=clr
    def details(self):      #method belirtildi
        print("my"+ self.name+"is"+self.colour)

apple= Fruit("apple","red")

apple.details()
