class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :二分法
        """
        lth = len(nums)
        if nums[0] < nums[lth-1] or lth == 1:
            return nums[0]

        if nums[int(lth/2)] < nums[int(lth/2)-1]:
            return nums[int(lth/2)]
        else:
            if nums[int(lth/2)] > nums[0]:
                return self.findMin(nums[int(lth/2):])
            else:
                return self.findMin(nums[:int(lth/2)])
if __name__=="__main__":
    # a = [4,5,6,7,0,1,2]
    a = [0,1]
    obj = Solution()
    b = obj.findMin(a)
    print(b)