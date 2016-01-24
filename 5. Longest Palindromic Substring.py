class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        maxnum = 0
        maxloc = [0,maxnum-1]
        j = len(s)-1
        for i in range(len(s)):
            if i+maxnum > len(s):
                break
            j = len(s)-1
            while j >= i+maxnum:
                if self.isPalidrome(s,i,j):
                    maxloc[0],maxloc[1] = i,j
                    maxnum = j-i+1
                    break
                j-= 1
            # print (maxnum)
        # print(maxloc[0],maxloc[1])
        return s[maxloc[0]:maxloc[1]+1]

    def isPalidrome(self,s,a,b):
        for i in range((b+1-a)//2):
            if s[a+i] != s[b-i]:
                return False
        return True

if __name__ == "__main__":
    a = "jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx"
    obj = Solution()
    print(obj.longestPalindrome(a))
    # print(obj.isPalidrome(a,1,4))