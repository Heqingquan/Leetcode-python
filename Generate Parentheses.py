class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.allParenthesis = []
        self.N = n
        self.addParenthesis('',0)
        return sorted(self.allParenthesis)
    def addParenthesis(self,string,n):
        if n == self.N:
            self.allParenthesis.append(string)
            return
        self.addParenthesis('('+string+')',n+1)
        if '('+string+')' != '()'+string:
            if '()'+string == string+'()':
                self.addParenthesis('()'+string,n+1)
            else:
                self.addParenthesis('()'+string,n+1)
                self.addParenthesis(string+'()',n+1)

if __name__ == "__main__":
    obj = Solution()
    b = obj.generateParenthesis(4)
    print(b)