class Solution:
    # @param board : tuple of strings
    # @return an integer
    def isValidSudoku(self, board):
        if len(board) != 9:  # check number of rows in the input
            return 0
        for i in range(9):
            for j in range(9):
                if(board[i][j]!='.'):
                    n=int(board[i][j])
                    for k in range(9):
                        if(( board[i][k]!='.' and n== int(board[i][k]) and j!=k) or (board[k][j]!='.' and n==int(board[k][j]) and i!=k )):
                            return 0
        l=[]
        for b in range(9):
            l[:]=[]
            n=b//3*3
            for i in range(n,n+3):
                m=b%3*3
                for j in range(m,m+3):
                    if(board[i][j]!='.' and board[i][j] in l):
                        return 0
                    else:
                        l.append(board[i][j])
        return 1

