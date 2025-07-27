class Human:
    species="Human"
    def __init__(self,name,age,name1):
        self.name=name
        self.name1=name1
        self.age=age
    def display(self):
        print("The name of the person is:",{self.name})
class Men(Human):
    def play(self):
        print("Man's name:",self.name)
        print("Men pay cricket.")
class Women(Human):
    def playtennis(self):
        print("Woman's age and name:",self.age,self.name1)
        print("Women play tennis")
class children(Men,Women):
    def playhop(self):
        print("Child's name:",self.name)
        print("Children play hopscotch")

men=Men("antony","Jessi",29)
men.display()
men.play()
women=Women("mark","jessica",30)
women.display()
women.playtennis()
child=children("sam","san",30)
child.display()
child.play()
child.playtennis()
child.playhop()