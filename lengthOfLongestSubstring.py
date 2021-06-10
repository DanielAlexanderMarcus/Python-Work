class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string=''
        lst=[]
        length_outer=0
        length_inner=1
        final=0
        s=str(s)
        while length_outer<=len(s)-1:
            length_inner=length_outer+1
            while length_inner<=len(s):  
                string=string+s[length_outer:length_inner]  
                for i in string:
                    lst.append(i)
                if len(set(lst))>final:
                    if len(lst)==len(set(lst)):
                        if len(lst)>final:
                            final=len(lst)
                length_inner=length_inner+1
                string=''
                lst=[]
            length_outer=length_outer+1  
        return final
