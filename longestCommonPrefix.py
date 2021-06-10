class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lst=[]
        lst_final=[]
        length=0
        string=''
        for i in strs:
            i=str(i)
            while length<len(i):
                string=string+i[length]
                lst.append(string)
                length=length+1
            string=''
            length=0
        for i in lst:
            if lst.count(i)==len(strs):
                if i not in lst_final:
                    lst_final.append(i) 
        for i in lst_final:
            if len(i)>len(string):
                string=i
        print(string)        
        return string
