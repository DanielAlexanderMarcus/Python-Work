class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        string=''
        s=str(s)
        negative=0
        final=0
        plus=0
        string_final=''
        if s.replace(' ','') in ('','-','+'):
            return 0
        s=s.lstrip(' ')
        for i in s:
            if len(string)==0:
                if i.isdigit()<>1:
                    if i=='-':
                        if plus==1 or negative==1:
                            return 0
                        else:
                            negative=1
                    elif i=='+':
                        if negative==1 or plus==1:
                            return 0
                        else:
                            plus=1
                            continue
                    else:
                        return 0
                else:
                    string=string+i
                        
            else:
                if i.isdigit()==0:
                    string_final=string
                    break
                else:
                    string=string+i
     
        
        if string_final=='':
            string_final = int(string)
        else:
            string_final = int(string_final)
        if string_final >= 2**31:
            if negative==1:
                string_final=2**31
            else:
                string_final=2**31-1
        else:
            string_final= int(string_final)
        
        if negative==1:
            string_final=string_final*-1
        
        return string_final    
            
        
