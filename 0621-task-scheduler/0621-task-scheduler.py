class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter

        freq = Counter(tasks)

        # Maximum frequency of any task
        max_freq = max(freq.values())

        # Count how many tasks have maximum frequency
        max_count = list(freq.values()).count(max_freq)

        # Formula:
        # (max_freq - 1) * (n + 1) + max_count
        intervals = (max_freq - 1) * (n + 1) + max_count

        # Answer should be at least total tasks
        return max(intervals, len(tasks))