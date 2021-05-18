class Solution:
    def twoSum(self, nums, target):
        outer = len(nums)-1
        inner = 0
        first = 0
        second = 0
        final=[]
        while outer>=0:
            first = nums[outer]
            inner = outer -1
            while inner >= 0:
                second = nums[inner]
                if first + second == target:
                    final.append(inner)
                    final.append(outer)
                    return final
                else:
                    inner=inner-1
            outer = outer -1 
