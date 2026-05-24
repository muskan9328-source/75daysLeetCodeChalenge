import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Create a min heap with first k elements
        heap = nums[:k]
        heapq.heapify(heap)

        # Process remaining elements
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # Root of heap is kth largest
        return heap[0]