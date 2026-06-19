class Solution:
    def getSum(self, a, b):
        mask = 0xffffffff
        max_int = 0x7fffffff

        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)