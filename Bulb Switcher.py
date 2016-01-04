import math as ml
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(ml.sqrt(n))
        '''
        Cn = [0 for i in range(n)]
        for i in range(1,n+1):
            k = 1
            while k*i < n+1:
                Cn[k*i-1] = Cn[k*i-1]^1
                k += 1
            # print (Cn)
        Count = 0
        for i in range(n):
            if Cn[i] == 1:
                Count += 1
        return Count
        '''

if __name__=="__main__":
    a = 99999
    b = [0 for i in range(100)]
    obj = Solution()
    for i in range(100):
        b[i] = obj.bulbSwitch(i)
    print(b)

