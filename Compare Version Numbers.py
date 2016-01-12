class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(min(len(v1),len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
        if len(v1) == len(v2):
            return 0
        elif len(v1) > len(v2):
            for i in range(len(v2),len(v1)):
                if int(v1[i]) != 0:
                    return 1
            return 0
        else:
            for i in range(len(v1),len(v2)):
                if int(v2[i]) != 0:
                    return -1
            return 0
if __name__ == "__main__":
    a1 = "1.453"
    a2 = "1.453.1"
    obj = Solution()
    print(obj.compareVersion(a1,a2))
