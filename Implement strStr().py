'''
依次匹配即可
最佳算法应该为KMP算法
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == len(needle) == 0:
            return 0
        Done = True
        for i in range(len(haystack)):
            Done = True
            if i+len(needle) >len(haystack):
                break
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    Done = False
                    break
            if Done:
                return i
        return -1
        