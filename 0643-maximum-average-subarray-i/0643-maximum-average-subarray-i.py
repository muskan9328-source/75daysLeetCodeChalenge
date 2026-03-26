class Solution(object):
    def findMaxAverage(self, nums, k):
        # Step 1: First window ka sum
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Step 2: Sliding window
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add next element
            window_sum -= nums[i-k]    # remove previous element
            
            max_sum = max(max_sum, window_sum)
        
        # Step 3: Return average
        return float(max_sum) / k