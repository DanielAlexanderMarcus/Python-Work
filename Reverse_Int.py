class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)
        b=""
        y=""
        
        if x[0]=='-':
            y=x[0]
            x=x[1:len(x)]
        
        for i in x:
            b = i + b
        b = y + b
        b = int(b)
        if -2**31 <= b <= 2**31 - 1:
            return b
        else:
            return 0
