class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = str(x) if x>=0 else str(x)[1:]
        l1 = ''.join(list(reversed(l)))
        x2 = int(l1) if x>0 else -int(l1)
        if x2 > (1<<31) or x2 < -(1<<31):
        	return 0
        else:
        	return x2


if __name__ == "__main__":
    # a = [-2,1,-3,4,-1,2,1,-5,4]
    # a = [-2,1]
    # a = [1]
    obj = Solution()
    b = obj.reverse(1)
    print(b)
