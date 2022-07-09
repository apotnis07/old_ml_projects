mydict={}

am = int(input("Enter mom's evaluation"))
pm = int(input("Enter dad's evaluation"))

def compound(am,pm):
    #years = int(input("Enter the number of years"))
    years=10
    #interest = int(input("Enter the interest"))
    interest=10
    interest = interest / 100;

    part = pow((1 + interest), years);
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


na,np,pa,pp=compound(am-15,pm)

t = totalpro(pa,pp)

#newa,newp,profita,profitp=compound(am,pm)


def deduct(am,pm,t):
    """x = int(input("Enter the amount to be deducted from anjali"))
    am = am - x
    y = int(input("Enter the amount to be deducted from pradeep"))
    pm = pm - y"""
    ded=20
    reseta=am
    resetp=pm
    #ded = int(input("Enter the amount to be deducted"))
    #for i in range (0,ded):
    #    for j in range(ded,0,-1):
    j=0
    for i in range(ded,0,-1):
            am = am - j
            print("Am=",am,"J=",j)
            pm = pm - i
            print("Pm=",pm,"I=",i)
            newa,newp,profita,profitp =compound(am,pm)
            tp = totalpro(profita,profitp)
            if (tp > t):
                diffa=reseta-am
                diffp=resetp-pm
                print("I=",diffa,"J=",diffp)
                print("Test=",tp)
                print("Standard=",t)
                print("Tp=",tp)
            am=reseta
            pm=resetp
            j = j+1

deduct(am,pm,t)

""""
for i in range(1,15):
    am-
"""