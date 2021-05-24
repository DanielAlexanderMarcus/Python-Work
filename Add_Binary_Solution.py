class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=str(a)
        aInt=0
        iterator=1
        lenA=len(a)
        for i in a:
            if i=='1':
               aInt=aInt+(2**(lenA-iterator))
            iterator=iterator+1
            
        b=str(b)
        bInt=0
        iterator=1
        lenb=len(b)
        for i in b:
            if i=='1':
               bInt=bInt+(2**(lenb-iterator))
            iterator=iterator+1
        
        
        lst=[]
        lstfinal=[]
        intsum=aInt+bInt
        original=intsum
        print(intsum)
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

 
