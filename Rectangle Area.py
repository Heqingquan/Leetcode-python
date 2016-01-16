class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rect_min_x1 = min(E,G)
        rect_max_x1 = max(E,G)

        rect_min_y1 = min(H,F)
        rect_max_y1 = max(H,F)

        rect_min_x2 = min(A,C)
        rect_max_x2 = max(A,C)

        rect_min_y2 = min(B,D)
        rect_max_y2 = max(B,D)
        delta_x = self.findCover(rect_min_x1,rect_max_x1,rect_min_x2,rect_max_x2)
        delta_y = self.findCover(rect_min_y1,rect_max_y1,rect_min_y2,rect_max_y2)
        area_1 = (rect_max_x1 -rect_min_x1) * (rect_max_y1-rect_min_y1)
        area_2 = (rect_max_x2 - rect_min_x2) * (rect_max_y2-rect_min_y2)
        return area_1+ area_2 - delta_x*delta_y

    def findCover(self,mi1,mx1,mi2,mx2):
        if mi2 >= mx1 or mx2 <= mi1:
            return 0
        if mx1 > mi2 and mi2 >= mi1 and mx1 <= mx2:
            return mx1-mi2
        if mi1 >= mi2 and mx2 >= mx1:
            return mx1-mi1
        if mi1 <= mi2 and mx1 >= mx2:
            return mx2-mi2
        if mx2 <= mx1 and mx2 > mi1 and mi1 >= mi2:
            return mx2-mi1

if __name__ == "__main__":
    a=b=c=d=0
    e=f =-1
    g=h = 1
    obj = Solution()
    print (obj.computeArea(a,b,c,d,e,f,g,h))