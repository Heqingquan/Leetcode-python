class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = [0 for i in range(len(digits)+1)]
        flag = 0
        digits[len(digits)-1] += 1
        for i in range(len(digits)-1,-1,-1):
            ans[i+1] = (digits[i]+flag) % 10
            flag = (digits[i]+flag) // 10
        ans[0] = flag
        return ans if ans[0] != 0 else ans[1:]

if __name__ == "__main__":
    # a = [9,9,9,9]
    a = [1,0,0,0,0,0,0]
    obj = Solution()
    b = obj.plusOne(a)
    print(b)

