class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        P = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            P[i][n-1] = 1
        for i in range(n):
            P[m-1][i] = 1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                P[i][j] = P[i][j+1]+P[i+1][j]
        return P[0][0]

if __name__ == "__main__":
    a,b = 4,4
    obj = Solution()
    print(obj.uniquePaths(a,b))
