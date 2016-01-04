class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.l ==[]:
            self.l.append(num)
        else:
            for i in range(len(self.l)):
                if num < self.l[i]:
                    break
            self.l.insert(i,num)
        
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        mid = int(len(self.l)/2)
        if len(self.l)%2 == 0:
            return (self.l[mid]+self.l[mid-1])/2
        else:
            return self.l[mid]
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
if __name__ == '__main__':
    mf = MedianFinder()
    for i in range(100,1,-1):
        mf.addNum(i)
        print(mf.findMedian())