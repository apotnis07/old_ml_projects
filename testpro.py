import string
a=[]

test='2+2'
x=len(test)
sum=0
for i in range(x):
    if test[i]=='+':

        a.append(test[0:i])

        a.append(test[i+1:x+1])

sum=int(a[0])+int(a[1])

print(x)
print(a)
print(test)
print(sum)

