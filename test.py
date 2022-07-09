import string
while True:
    print("1.Palindrome")
    print("2.Factorial")
    print("3.Pattern")
    print("4.Exit")
    ch=int(input("Enter the choice"))
    if ch==1:
        a=[]
        a=input("Enter the string")
        if a == a[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")
    elif ch==2:
        b=int(input("Enter the number of which the factorial is to be calculated"))
        for i in range(1,b):
            b=b*i
            print(i)
        print(b)
    elif ch==3:
        for i in range(4):
            for j in range(i+1):
                print("*",end="")
            print("\r")

    elif ch==4:
        break
    else:
        print("Invalid choice")
