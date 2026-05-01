class dog:
     def __init__(self,name,age):
          self.name = name
          self.age = age
     def description(self):
      return f"{self.name}  is {self.age} Year old" 
my_dog = dog("Buddy",3)
print(my_dog.description())        

