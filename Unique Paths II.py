class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        zeroflag = 0
        for i in range(m-2,-1,-1):
            if zeroflag == 1:
                obstacleGrid[i][n-1] = 0
            else:
                if obstacleGrid[i][n-1] == 1:
                    obstacleGrid[i][n-1] = 0
                    zeroflag = 1
                else:
                    obstacleGrid[i][n-1] = 1
        zeroflag = 0
        print (obstacleGrid)
        for i in range(n-2,-1,-1):
            if zeroflag == 1:
                obstacleGrid[m-1][i] = 0
                continue
            if obstacleGrid[m-1][i] == 1:
                obstacleGrid[m-1][i] = 0
                zeroflag = 1
            else:
                obstacleGrid[m-1][i] =1
        print (obstacleGrid)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                obstacleGrid[i][j] = obstacleGrid[i+1][j]+obstacleGrid[i][j+1]
        print(obstacleGrid)
        return obstacleGrid[0][0]

if __name__ == "__main__":
    # a = [[0,0],[1,1],[0,0]]
    a = [[0,0]]
    obj = Solution()
    print(obj.uniquePathsWithObstacles(a))
