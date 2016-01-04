class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        isPalidromeTable = [[0 for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i,len(s)):
                isPalidromeTable [i][j] = self.isPalidrome(s,start,end)
    def isPalidrome(self,s,start,end):
        for i in range((end-start+1)//2):
            if s[i+start] != s[end-i]:
                return 0
        return 1

if __name__ == "__main__":
    a = "abccba"
    # a = 'a'
    obj = Solution()
    b = obj.isPalidrome(a,3,3)
    print(b)


