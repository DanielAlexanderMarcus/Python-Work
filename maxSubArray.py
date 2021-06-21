class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        integer = 0
        number = 0
        final = None
        position = 0
        for i in nums:
            number=number+1
            position=number
            integer = i
            if integer > final:
                final = integer
            while position<=len(nums)-1:
                integer = integer + nums[position]
                if integer > final:
                    final = integer
                position=position+1
        return final
