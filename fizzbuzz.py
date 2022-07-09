a,b=input().split()
a=int(a)
b=int(b)
d=1
for i in range(0,a):
    for j in range(0,b):
        if(j==b-1):
            print(d,end="")
            d=d+1
        else:
            print(d,end=" ")
            d=d+1
    if(i!=a-1):
        print()

