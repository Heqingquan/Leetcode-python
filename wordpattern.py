class Solution(object):
    def wordPattern(self, pattern, str1):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordlist = str1.split(' ')
        if len(pattern) != len(wordlist):
        	return False
        #print(wordlist)
        for i in range(len(pattern)-1):
        	for j in range(i,len(pattern)):
        		if (pattern[i] == pattern[j] and wordlist[i] != wordlist[j])\
        		or (wordlist[i] == wordlist[j] and pattern[i] != pattern[j]):
        		    #print(str(i) + '   ' + str(j))
        		    #print (pattern[i]+pattern[j]+wordlist[i]+wordlist[j])
        		    return False
        return True




if __name__ == '__main__':
	str1 = "dog cat cat dog"
	pattern = "abba"
	test = Solution()
	if test.wordPattern(pattern,str1):
		print ("hello")
	else:
		print("world")
