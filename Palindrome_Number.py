class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=str(x)
        b = ""
        for i in a:
            b = i + b

        if a==b:
            return 1
        else: 
            return 0
          
