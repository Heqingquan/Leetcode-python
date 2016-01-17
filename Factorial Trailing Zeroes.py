class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.trailingZeroes(n/5)+n/5 if n >= 5 else 0
