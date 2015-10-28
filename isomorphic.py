class Solution(object):
    def isIsomorphic(self, pattern, str1):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str1):
        	return False
        if pattern == "":
            return True
        dictstr = {pattern[0]:0}
        for i in range(1,len(pattern)):
            if not pattern[i] in dictstr:
                for j in dictstr.values():
                    if str1[i] == str1[j]:
                        #print (dictstr.values())
                        return False
                dictstr[pattern[i]] = i
            else:
                loc = dictstr[pattern[i]]
                if str1[i] != str1[int(loc)]:
                    return False
        return True




if __name__ == '__main__':
	str1 = "paper"
	pattern = "title"
	test = Solution()
	if test.isIsomorphic(pattern,str1):
		print ("hello")
	else:
		print("world")
