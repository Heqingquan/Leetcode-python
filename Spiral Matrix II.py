class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        c_list = [[0 for i in range(n)] for j in range(n)]
        count = 1
        i = 0;
        j = 0;
        while 1:
            while j<n and c_list[i][j] == 0:
                c_list[i][j] = count
                count += 1
                j += 1
            j-= 1
            i+= 1
            while i<n and c_list[i][j] == 0:
                c_list[i][j] = count
                count += 1
                i+= 1
            i-= 1
            j-= 1
            while j>=0 and c_list[i][j] == 0:
                c_list[i][j] = count
                count += 1
                j -= 1
            j += 1
            i -= 1
            while i>=0 and c_list[i][j] == 0:
                c_list[i][j] = count
                count += 1
                i-= 1
            i += 1
            j += 1
            if count > n**2:
                break
        return c_list

if __name__ == "__main__":
    a = "rabbit"
    b = "rabbbit"
    obj = Solution()
    print(obj.generateMatrix(3))
