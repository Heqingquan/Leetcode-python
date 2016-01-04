class Solution(object):
    def numDecodings(self, string):
        if len(string) == 0:
            return 0
         if int(string[0]) == 0:
            return 0
        if len(string) == 1:
            return 1
        i = 1
        ans = 1
        flag = 0
        count = 1
        while i<len(string):
            if int(string[i]) == 0 and int(string[i-1]) == 0:
                return 0

            if self.isDecode(string,i):
                count += 1
                flag = 1
            else:
                ans *= self.Feb(count)
                count = 1
                flag = 0
            i += 1
        if flag == 1:
            return self.Feb(count)
        return ans
    def isZero(self,string,i):


    def isDecode(self,string,i):
        if int(string[i-1]) == 1 and int(string[i]) != 0:
            return True
        if int(string[i-1]) == 2 and int(string[i]) != 0 and int(string[i])<7:
            return True
        return False
    def Feb(self,n):
        a = 1
        b = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        while n != 2:
            c = a+b
            a,b = b,c
            n -= 1
        return c

if __name__ == "__main__":
    string = "0"
    obj = Solution()
    print(obj.numDecodings(string))