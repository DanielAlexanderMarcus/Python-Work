class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        inner_length=1
        outer_length=0
        string=''
        final=''
        lst=[]
        lst_r=[]
        s=str(s)
        while outer_length<=len(s)-1:
            inner_length=outer_length+1
            while inner_length<=len(s):
                string=string+s[outer_length:inner_length]
                for i in string:
                    lst.append(i)
                for i in reversed(lst):
                    lst_r.append(i)
                if lst == lst_r:
                    if len(string)>=len(final):
                        final=string
                inner_length=inner_length+1
                lst=[]
                lst_r=[]
                string=''
            outer_length=outer_length+1
        return final
