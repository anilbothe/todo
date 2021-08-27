# class Myclass:
#     x = 3
#     t = 4
# p1 = Myclass()
# print(p1.x) 
# print(p1.t)

# class Myclass:
#     def __init__(self, name, age):
#       self.name = name
#       self.age = age
# x = str(input("enter the name: "))
# y = int(input("enter age : "))
# p1 = Myclass(x, y)
# print(p1.name)
# print(p1.age)    

# class Myclass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunction(self):
#         print("my name is " + self.name)
#         print(f"my age is {self.age}")
# x = str(input("enter name : "))
# y = int(input("enter age : "))    
# p1 = Myclass(x, y) 
# p1.myfunction()    

class Myclass:
    def __init__(mysillyobjiect, name, age):
        mysillyobjiect.name = name
        mysillyobjiect.age = age
    def myfunction(abc):
        print("my name is " + abc.name) 
        print(f"my age is {abc.age}")
x = str(input("enter name : "))
y = int(input("enter age : "))        
p1 = Myclass(x, y)
p1.myfunction()            




           