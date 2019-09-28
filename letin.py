from string import *

#print(alpha)

def getlet(let,alpha):
    #print("\n[",alpha," ]")
    for i in range(len(alpha)):
        if alpha[i]==let:
            a=alpha[:i]
            b=alpha[i+1:]
            alpha=a+"*"+b
    #print(alpha)
    return alpha

#alpha=getlet(alpha)
#prin   t("2")
#alpha=getlet(alpha)
