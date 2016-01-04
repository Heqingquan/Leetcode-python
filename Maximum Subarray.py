class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = -99999999
        cache = 0
        for i in nums:
            cache += i
            if cache > data:
                data = cache
            if cache < 0:
                cache = 0
        return data

if __name__ == "__main__":
    a = [-2,1,-3,4,-1,2,1,-5,4]
    # a = [-2,1]
    a = [1]
    obj = Solution()
    b = obj.maxSubArray(a)
    print(b)
