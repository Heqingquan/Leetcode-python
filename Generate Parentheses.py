class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.allParenthesis = []
        self.N = n
        self.addParenthesis('',n,n,0)
        return self.allParenthesis
        
    def addParenthesis(self,string,lft,rht,n):
        if n == 2*self.N:
            self.allParenthesis.append(string)
            return
        if lft == rht:
            self.addParenthesis(string+'(',lft-1,rht,n+1)
        if lft < rht:
            if lft > 0:
                self.addParenthesis(string+'(',lft-1,rht,n+1)
            self.addParenthesis(string+")",lft,rht-1,n+1)
       
if __name__ == "__main__":
    obj = Solution()
    b = obj.generateParenthesis(4)
    print(b)