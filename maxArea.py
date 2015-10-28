'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height:List[int]
        :rtype: int
        """
        flag = 0
        forwardflag = 0
        backwardflag = len(height)-1
        value = 0
        while forwardflag < backwardflag:
            if value < min(height[backwardflag],height[forwardflag]) * (backwardflag-forwardflag):
                value = min(height[backwardflag],height[forwardflag]) * (backwardflag-forwardflag)
            else:
                if height[backwardflag] > height[forwardflag]:
                    forwardflag +=1
                else:
                    backwardflag -=1
        return value






if __name__ == '__main__':
	pattern = [1,2,11,13,1,10,10,9,8]
	test = Solution()
	print( test.maxArea(pattern))