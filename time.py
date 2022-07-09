a,b=input("Time when you started in hours and minutes").split()
a=int(a)
b=int(b)

c,d=input("Time now in hours and minutes").split()
c=int(c)
d=int(d)
#time.strftime('%I:%M:%S %p %Z')

if(b>d):
    c=c-1
    minutes=(d+60)-b
    hours=c-a
else:
    hours=c-a
    minutes=d-b
print("You were engaged in the activity for",hours,"hours and",minutes,"minutes")
