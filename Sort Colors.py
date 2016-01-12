class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for i in nums:
            if i == 0:
                red += 1
            if i == 1:
                white += 1
            if i == 2:
                blue += 1
        for i in range(red):
            nums[i] = 0
        for i in range(red,red+white):
            nums[i] = 1
        for i in range(red+white,red+white+blue):
            nums[i] = 2

if __name__ == "__main__":
    a = [0,1,2,0,1,2]
    obj = Solution()
    obj.sortColors(a)
    print (a)