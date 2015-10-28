import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
        	return False
        cache = [0 for i in range(len(s))]
        cache_count = 0;
        for i in range(len(s)):
        	if s[i].isdigit() or s[i].isalpha():
        		cache[cache_count] = s[i].lower()
        		cache_count += 1
        s1 = cache[:cache_count]
        #print (s1)
        for i in range (int(len(s1)/2)):
        	if s1[i] != s1[len(s1)-1-i]:
        		return False
        return True



if __name__ == '__main__':
	str1 = "A man, a plan, a canal: Panama"
	test = Solution()
	if test.isPalindrome(str1):
		print ("hello world")
	else:
		print ("Wrong")