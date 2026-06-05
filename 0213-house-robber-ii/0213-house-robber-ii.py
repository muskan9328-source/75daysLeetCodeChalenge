class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev1 = 0
            prev2 = 0

            for num in arr:
                temp = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = temp

            return prev1

        return max(
            helper(nums[:-1]),  # first include, last exclude
            helper(nums[1:])    # first exclude, last include
        )