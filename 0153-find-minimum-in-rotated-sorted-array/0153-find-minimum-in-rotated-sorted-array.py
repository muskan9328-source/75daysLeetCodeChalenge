class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than right → min is on right side
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Min is at mid or on left side
                right = mid
        
        return nums[left]