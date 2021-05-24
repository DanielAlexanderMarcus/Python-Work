def Binary_to_Base_Ten(a):
    a=str(a)
    aInt=0
    iterator=1
    lenA=len(a)
    for i in a:
        if i=='1':
           aInt=aInt+(2**(lenA-iterator))
        iterator=iterator+1
    return aInt
            
 
def Sum_to_Binary(a,b):
    lst=[]
    lstfinal=[]
    intsum=a+b
    original=intsum
    iterator=0
    while intsum>=1:
        lst.append(2**iterator)
        intsum=intsum/2
        iterator=iterator+1
    length=len(lst)-1
    if original==0:
        lstfinal.append(0)
    while length>=0:
        if original-lst[length]>=0:
            lstfinal.append(1)
            original=original-lst[length]
        else:
            lstfinal.append(0)
        length=length-1
    final=""
    for i in lstfinal:
        final=final+str(i)
        
    return final

a=Sum_to_Binary(Binary_to_Base_Ten(0), Binary_to_Base_Ten(0))
print(a)
