class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False
        
        # Frequency arrays
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Fill frequency for s1 and first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        
        # Check first window
        if s1_count == window_count:
            return True
        
        # Sliding window
        for i in range(len(s1), len(s2)):
            # Add new character
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # Remove old character
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            # Compare
            if s1_count == window_count:
                return True
        
        return False