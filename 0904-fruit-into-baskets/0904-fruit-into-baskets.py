class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        left = 0
        max_fruits = 0
        basket = {}

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # Agar 2 se zyada fruit types ho jaye
            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits