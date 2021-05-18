class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        finalarray=[]
        finalint=0
        length=0
        maxlen=len(digits)-1
        while length <= len(digits)-1 and maxlen >= 0:
            finalint = finalint + (digits[length]*10**maxlen)
            length = length + 1
            maxlen = maxlen-1
        finalint = str(finalint + 1)
        for i in finalint:
            finalarray.append(i)
        return finalarray
