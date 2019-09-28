#Module to store words from file to dictionary

def wordbank(i,admin='n'):
    f=open("dict.txt",'r')
    l=f.readline()
    a={}
    j=1
    while l:
        a[j]=l
        l=f.readline()
        j+=1
    if admin=='a':
        return a
    else:
        return a.get(i)
    #print(a.get(i))
    #print(a)

#print(wordbank(1))
#wordbank(1)
