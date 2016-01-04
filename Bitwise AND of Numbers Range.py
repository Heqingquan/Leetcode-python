class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n: 
            return m
        dx = self.findIndex(n-m+1)
        return (m>>dx&n>>dx)<<dx if (n-m+1) == (1<<dx) else (m>>(dx+1)&n>>(dx+1))<<(dx+1)




    def findIndex(self,x):
        count = 0
        while x != 1:
            x = x >> 1
            count += 1
        return count

if __name__ == "__main__":
    a = 3
    obj = Solution()
    print(obj.rangeBitwiseAnd(6,7))