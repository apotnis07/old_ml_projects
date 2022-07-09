
while True:
    print("1.Even and odd")
    print("2.Merge and sort")
    print("3.Update first element")
    print("4.Max and Min")
    print("5.Python")
    print("6.Exit")

    ch = int(input("Enter the choice"))
    if ch == 1:
        a = []
        e = []
        o = []

        n=int(input("Enter the number of elements"))
        for i in range(0,n):
            print("Enter the element")
            x=int(input())
            if x%2==0:
                e.append(x)
            elif x%2!=0:
                o.append(x)
        print("Even=",e)
        print("Odd=", o)
    if ch==2:
        e=[]
        o=[]
        a=[]
        n = int(input("Enter the number of elements in first list"))
        for i in range(0, n):
            print("Enter the element")
            x = int(input())
            e.append(x)
        n = int(input("Enter the number of elements in second list"))
        for i in range(0, n):
            print("Enter the element")
            x = int(input())
            o.append(x)
        a=e+o
        print(a)
        a.sort()
        print(a)
    elif ch==3:
        e=[]
        n = int(input("Enter the number of elements in first list"))
        for i in range(0, n):
            print("Enter the element")
            x = int(input())
            e.append(x)
        e.pop(0)
        y=int(input("Enter the value at one"))
        e.insert(0,y)
        print(e)
        e.pop(n-1)
        print(e)
    elif ch==4:
        e = []
        n = int(input("Enter the number of elements in first list"))
        for i in range(0, n):
            print("Enter the element")
            x = int(input())
            e.append(x)
        e.sort(reverse=True)
        print("The max is :",e[0])
        print("The min is :",e[n-1])


    elif ch==5:
        e = []
        n = int(input("Enter the number of elements in first list"))
        for i in range(0, n):
            print("Enter the element")
            x = input()
            e.append(x)
        for i in range(0,n):
            if e[i]=='python':
                print("found")

    elif ch==6:
        break
    else:
        print("Invalid response")










