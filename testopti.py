mydict={}
am = int(input("Enter mom's evaluation"))
pm = int(input("Enter dad's evaluation"))

def compound(am,pm,i):
    #years = int(input("Enter the number of years"))
    years=10
    #interest = int(input("Enter the interest"))
    interest=10
    interest = interest / 100;

    part = pow((1 + interest), i);
    compoundam = am * part;
    compoundpm = pm * part;
    profita = compoundam - am
    profita=round(profita)
    profitp = compoundpm - pm
    profitp=round(profitp)
    newa = round(compoundam, 2)
    newp = round(compoundpm, 2)
    #mydict['Mom new']=newa
    #mydict['Dad new']=newp
    #mydict['Mom profit'] = profita
    #mydict['Dad profit'] = profitp
    #print(mydict)
    return newa,newp,profita,profitp


def totalpro(profita, profitp):
    totalprofit = profita + profitp
    totalprofit = round(totalprofit)
    #print("Total_profit =", totalprofit)
    return totalprofit
reseta=am
resetp=pm

for i in range(0,10):
    na,np,pa,pp=compound(am-15,pm,i)
    #print(na)
    #print(np-pm)
    t = totalpro(pa, pp)
    print(t)
    if (t>15):
        print("Na=",na)
        print("Np=",np)
        print("Year=",i)



        break

    am = reseta
    pm = resetp





