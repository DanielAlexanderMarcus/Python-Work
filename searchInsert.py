class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos=-1
        for i in nums:
            if target==i:
                pos=nums.index(i)
        if pos==-1:
            nums.append(target)  
            nums=sorted(nums)
            pos=nums.index(target)
        return int(pos)
