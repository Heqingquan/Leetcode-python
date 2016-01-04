class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        l_s = len(s)
        l_t = len(t)

        c_list = [[0 for i in range(l_s+1)] for j in range(l_t+1)]
        c_list[0][0] = 1
        for i in range(1,l_t+1):
            for j in range (1,l_s+1):
                if s[j-1] == t[i-1]:
                    c_list[i][j] = sum(c_list[i-1][:j])
        return sum(c_list[l_t])

if __name__ == "__main__":
    a = "rabbit"
    b = "rabbbit"
    obj = Solution()
    print(obj.numDistinct(b,a))




