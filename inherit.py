class Person:
    def __init__(self,name,rn,m1,m2):
        self.name=name
        self.rn=rn
        self.m1=m1
        self.m2=m2
    def read(self):
        self.name=input("Enter your name")
        self.rn=int(input("Enter your roll no"))
        self.m1=int(input("Enter subject 1 marks out of 100"))
        self.m2=int(input("Enter subject 2 marks out of 100"))
    def display(self):
        print(self.name)
        print(self.rn)
        print(self.m1)
        print(self.m2)

class Result(Person):
    def __init__(self,name,rn,m1,m2,total,percent):
        self.total=total
        self.percent=percent
        super().__init__(name,rn,m1,m2)
    def calculatepercent(self):
        self.total=self.m1+self.m2
        self.percent = (self.total / 200) * 100

    def displaypercent(self):
        print(self.percent)
name=''
rn=0
m1=0
m2=0
total=0
percent=0
R1=Result(name,rn,m1,m2,total,percent)
R1.read()
R1.display()
R1.calculatepercent()
R1.displaypercent()


