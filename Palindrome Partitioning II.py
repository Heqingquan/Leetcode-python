class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        PalidromeTable = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(1,len(s)):
            for j in range(i-1,-1,-1):
                if self.isPalidrome(s,j,i) == 1:
                    PalidromeTable[j][i] = 0
                else:
                    minCount = 999999
                    for k in range(j,i):
                        num = PalidromeTable[j][k]+PalidromeTable[k+1][i]
                        minCount = min(minCount,num)
                    PalidromeTable[j][i] = minCount+1
                    # print (k)
            # print (PalidromeTable)
        # print (PalidromeTable)
        return PalidromeTable[0][len(s)-1]


    '''# 限界减枝算法，复杂度太高
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        isPalidromeTable = [[0 for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i,len(s)):
                isPalidromeTable [i][j] = self.isPalidrome(s,i,j)
        # print (isPalidromeTable)
        self.min = 999999
        #限界减枝搜索
        minflag = 0
        cutnum = 0
        self.findCutNum(isPalidromeTable,0,len(s)-1,-1)
        return self.min
    
    def findCutNum(self,Table,start,end,m):
        print (start, end ,m)
        m += 1
        if m>=self.min:
            return
        flag = self.searchMin(Table,start,start,end)
        if flag == len(Table)-1:
            if m<self.min:
                self.min = m
                return
        if flag == -1:
            return 
        self.findCutNum(Table,flag+1,end,m)
        if flag == start:
            return
        else:
            self.findCutNum(Table,0,flag-1,m)


    def searchMin(self,Table,x,y1,y2):
        for i in range(y2,y1-1,-1):
            if Table[x][i] == 1:
                return i
        return -1 
'''

    def isPalidrome(self,s,start,end):
        for i in range((end-start+1)//2):
            if s[i+start] != s[end-i]:
                return 0
        return 1

if __name__ == "__main__":
    # a = "hello world"
    # a = 'a'
    # a = "aaaaba"
    # a = "adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"
    a = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
    obj = Solution()
    # b = obj.isPalidrome(a,3,3)
    b = obj.minCut(a)
    print(b)


