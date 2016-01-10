class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        lth = len(triangle)
        count = [0 for i in range((lth**2+lth)//2)]
        sumation = 0
        j = 1
        count [0] = triangle[0][0]
        for l in triangle[1:]:
            for i in range(len(l)):
                # print (l)
                if i == 0:
                    count[j] = l[i] + count[j-len(l)+1]
                    j += 1
                    continue
                if i == len(l)-1:
                    count[j] = l[i] + count[j-len(l)]
                    j+= 1
                    continue
                count[j] =l[i] + min(count[j-len(l)+1],count[j-len(l)])
                j += 1
        # print (count)
        minium = count[-1]
        for i in range(1,lth+1):
            # print (i)
            if count[-i] < minium:
                minium = count[-i]
        return minium





        return sumation

if __name__ == "__main__":
    a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    obj = Solution()
    b = obj.minimumTotal(a)
    print(b)
