class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        place=0
        length=0
        value=""
        s=s.strip()
        if len(s.replace(" ",""))==0:
            return 0
        else:
            if " " in s:
                while length<=len(s)-1:
                    value=s[length]
                    if value==" ":
                        place=length
                    length=length+1
                return len(s[place+1: len(s)])
            else: 
                return len(s)
