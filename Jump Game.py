class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxnum = -1
        for i in range(len(nums)):
            if maxnum < nums[i] + i:
                maxnum = nums[i] + i
            if maxnum >= len(nums)-1:
                return True
            if maxnum <= i:
                return False


if __name__ == "__main__":
    a =[2,3,1,1,4]
    # a = [3,2,1,0,4]
    # a = [1,0,1,0]
    # print(len(a))
    obj = Solution()
    ans = obj.canJump(a)
    print(ans)
