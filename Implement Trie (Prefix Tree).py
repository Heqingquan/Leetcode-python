class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.endflag = [0 for i in range(26)]
        self.value = [0 for i in range(26)]
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        pre = node
        for w in word:
            pre = node
            if node.value[ord(w)-ord('a')] == 0:
                node.value[ord(w)-ord('a')] = TrieNode()
            node = node.value[ord(w)-ord('a')]
        pre.endflag[ord(w)-ord('a')] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            pre = node
            if node.value[ord(w)-ord('a')] == 0:
                return False
            node = node.value[ord(w)-ord('a')]
        if pre.endflag[ord(w)-ord('a')] == 1:
            return True
        else:
            return False

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for w in prefix:
            if node.value[ord(w)-ord('a')] == 0:
                # print ("hello")
                return False
            node = node.value[ord(w)-ord('a')]
        return True
        
if __name__ == "__main__":
# Your Trie object will be instantiated and called as such:
    trie = Trie()
    print (trie.insert("abc"))
    print (trie.search("ab"))
    print (trie.insert("ab"))
    print (trie.search("ab"))
    print (trie.startsWith("a"))