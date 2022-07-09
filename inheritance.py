class Person:
    def __init__(self,i,n):
        self.name=n
        self.id=i
    def display(self):
        print(self.name)
        print(self.id)


class Student(Person):
    def __init__(self,n,i,s1,s2):
        self.sub1=s1
        self.sub2=s2
        super().__init__(n,i)


    def display(self):
        super().display()
        print(self.sub1)
        print(self.sub2)

class Sports:
    def __init__(self,sm):
        self.smarks=sm

    def printsports(self):
        print(self.smarks)


class Result(Student,Sports):
    def __init__(self,n,i,s1,s2,sm):
        Student.__init__(self,n,i,s1,s2)
        Sports.__init__(self,sm)

    def total(self):
        sports=input("Have you participated in sports")
        if sports=="yes":
            sum=self.sub1+self.sub2+self.smarks
        else:
            sum=self.sub1+self.sub2
        print("Total=",sum)



id=int(input("Enter ID"))
name=input("Enter Name")
s1=int(input("Enter Subject 1 marks"))
s2=int(input("Enter Subject 2 marks"))
sm=int(input("Enter Sports marks"))
R1=Result(name,id,s1,s2,sm)
R1.display()
R1.printsports()
R1.total()