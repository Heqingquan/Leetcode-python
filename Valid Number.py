import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile(r"^\s*[+-]?(([0-9]+\.?[0-9]*)|([0-9]*\.?[0-9]+))(e[+-]?[0-9]+)?\s*$")
        ma = pattern.match(s)
        if ma:
            # print(ma.groups())
            return True
        else:
            return False

if __name__ == "__main__":
    a = "   3.e  1"
    obj = Solution()
    b = obj.isNumber(a)
    print(b)