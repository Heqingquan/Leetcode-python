import queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'
        serial = []
        s_queue = queue.Queue()
        s_queue.put(root)
        serial.append(root.val)
        while not s_queue.empty():
            node = s_queue.get()
            if node.left is None:
                serial.append('#')
            else:
                s_queue.put(node.left)
                serial.append(node.left.val)
            if node.right is None:
                serial.append('#')
            else:
                s_queue.put(node.right)
                serial.append(node.right.val)
        return serial


            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '#':
            return None
        root = TreeNode(data[0])
        s_queue = queue.Queue()
        s_queue.put(root)
        for i in range(1,len(data),2):
            node = s_queue.get()
            if data[i] == '#':
                node_l = None
            else:
                node_l = TreeNode(data[i])
                s_queue.put(node_l)
                node.left = node_l
            if data[i+1] == '#':
                node_r = None
            else:
                node_r = TreeNode(data[i+1])
                s_queue.put(node_r)
                node.right = node_r
        return root


if __name__ == '__main__':
    str1 = "123##45"
    test = Codec()
    print (test.serialize(test.deserialize(str1)))




        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))