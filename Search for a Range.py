class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = 0
        loc = self.findTarget(nums,target,0,len(nums)-1)
        if loc == -1:
            return [-1,-1]
        left = loc
        right = loc
        while left > -1 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1
        return [left+1,right-1]


    def findTarget(self,nums,target,start,end):
        # print (str(start) +"    " +str(end))
        if nums[(start+end)//2] == target:
            return (start+end)//2
        if start==end:
            return -1
        # print ("why")
        elif nums[(start+end)//2] > target:
            return self.findTarget(nums,target,start,(start+end)//2)
        else:
            return self.findTarget(nums,target,(start+end)//2+1,end)


if __name__ == "__main__":
    # num = [5, 7, 7, 8, 8, 10]
    num = [8, 8, 8, 8, 8, 8,8]
    # num = [1]
    # num = [2,2]
    target = 8
    obj = Solution()
    print(obj.searchRange(num,target))
