class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return ''.join(s)
        s1 = [0 for i in range(len(s))]
        count = 0;
        loc = 0;
        while(count*(2*numRows-2)<len(s)):
            s1[loc] = s[count*(2*numRows-2)] 
            count += 1
            loc+= 1
        count = 0

        for n in range(1,numRows-1):
            while(count*(2*numRows-2)+n<len(s)):
                s1[loc] = s[count*(2*numRows-2)+n] 
                if ((count+1)*(2*numRows-2)-n < len(s)):
                    loc+=1;
                    s1[loc] = s[(count+1)*(2*numRows-2)-n] 
                count += 1
                loc +=1
            count = 0
        count = 0
        while(count*(2*numRows-2)+(numRows-1)<len(s)):
            s1[loc] = s[count*(2*numRows-2)+(numRows-1)] 
            count += 1
            loc += 1
        count = 0
        return ''.join(s1)


        

if __name__ == '__main__':
	str1 = "ab"
	test = Solution()
	print (test.convert(str1,1))