class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= k:
            k = k % len(nums)
        subnums = nums[-k:]
        for i in range(len(nums)-1,k-1,-1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = subnums[i]

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7]
    b = 3
    obj = Solution()
    obj.rotate(a,b)
    print (a)
