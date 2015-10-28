'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

class Solution(object):
    def trap(self, height):
        """
        :type height:List[int]
        :rtype: int
        """
        solid = [0 for i in range(len(height))]
        down = 0
        up = 0
        for point in range(len(height-1)):
        	if height[point+1] < height[point]:
        		down = 1
        	elif height[point+1] >height[point]:
        		up = 1
        	if 
        	if down == 1 && up == 1:








if __name__ == '__main__':
	
	pattern = [1,2,11,13,1,10,10,9,8]
	test = Solution()
	print( test.trap(pattern))