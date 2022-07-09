import math
N,v1,v2=input().split()
N=int(N)
v1=int(v1)
v2=int(v2)
if(v1>=1 and v2<=100 and 1<=N and N<=200):
    #for arun
    da=math.sqrt(2)*N
    ta=(1.0*da)/v1
    #for taxi
    dt=2*N
    tt=(1.0*dt)/v2
    if(ta>tt):
        print("Cab")
    elif(ta<tt):
        print("Walk")
    else:
        print("Both take same time")
else:
    print("Condition not satisfied")