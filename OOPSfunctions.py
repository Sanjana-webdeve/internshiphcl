class Animal:
    species="Human"
    def __init__(self,name,age):
        self.name=name
        self.age=age

animal=Animal("Priya",30)
animalnew=Animal("Ravi",32)
print(animal.name)
print(animal.age)
print(animal.species)
print(animalnew.age)
print(animalnew.name)
print(animalnew.species)
animalnew.species="Male"
print(animalnew.species)
print(animal.species)


