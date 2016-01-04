class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                continue
            if num % 3 == 0:
                num = num // 3
                continue
            if num % 5 == 0:
                num = num // 5
                continue
            break
        if num == 1:
            return True
        else:
            return False
if __name__ == "__main__":
    obj = Solution()
    print(obj.isUgly(14))
        