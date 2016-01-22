class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == None:
            return
        n = len(board)
        if n == 0:
            return 
        m = len(board[0])
        if m == 0:
            return 
        boardCache = [[0 for i in range(m)] for j in range(n)] 
        for i in range(m):
            for j in range(n):
                self.updateboard(board,boardCache,i,j)
                # print("old",board)
                # print(i,j,boardCache)
        # print(boardCache)
        for i in range(n):
            for j in range(m):
                board[i][j] = boardCache[i][j]

    def updateboard(self,old,new,x,y):
        alive = 0
        if x-1 > -1 :
            if y-1 > -1 and old[y-1][x-1] == 1:
                alive += 1
            if old[y][x-1] == 1:
                alive += 1
            if y+1 < len(old) and old[y+1][x-1] == 1:
                alive += 1
        if x+1 < len(old[0]):
            if y-1 > -1 and old[y-1][x+1] == 1:
                alive += 1
            if old[y][x+1] == 1:
                alive += 1
            if y+1 < len(old) and old[y+1][x+1] == 1:
                alive += 1
        if y-1 > -1 and old[y-1][x] == 1:
            alive += 1
        if y+1 < len(old) and old[y+1][x] == 1:
            alive += 1
        # print (alive)
        if old[y][x] == 1:
            if alive < 2:
                # print("1")
                new[y][x] = 0
            if alive == 2 or alive == 3:
                # print("q")
                new[y][x] = 1
            if alive > 3:
                new[y][x] = 0
        else:
            if alive == 3:
                new[y][x] = 1
            else:
                new[y][x] = 0


if __name__ == "__main__":
    # a = [[1,1,1],[0,0,0],[1,1,1]]
    a = [[0,0]]
    obj = Solution()
    obj.gameOfLife(a)
    print(a)