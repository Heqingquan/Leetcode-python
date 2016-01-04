class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlth = 1
        count = 0
        while (count < len(s)):
            if count + maxlth > len(s):
                return maxlth-1
            if self.isDuplicate(s[count:count+maxlth]):
                count +=1
            else:
                maxlth += 1
        return maxlth-1

    def isDuplicate(self,s1):
        if len(set(s1)) != len(s1):
            return True
        else:
            return False



if __name__=="__main__":
    # a = [4,5,6,7,0,1,2]
    # a = "pwwkew"
    # a = "bbbbb"
    # a = "abcabcbb"
    a = "a"
    obj = Solution()
    b = obj.lengthOfLongestSubstring(a)
    print(b)