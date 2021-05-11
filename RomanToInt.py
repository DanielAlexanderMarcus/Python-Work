class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        b=0
        last = 0
        for i in s:
            if i=='I':
                i=1
            elif i=='V':
                i=5
            elif i=='X':
                i=10
            elif i=='L':
                i=50
            elif i=='C':
                i=100
            elif i=='D':
                i=500
            elif i=='M':
                i=1000
            if (last==1 and (i==5 or i==10)) or (last==10 and (i==50 or i==100)) or (last==100 and (i==500 or i==1000)):
                i = i-2*last
            b = b + i
            last=i
        return b
