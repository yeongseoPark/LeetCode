class Solution(object):
    def isValidSudoku(self, board):
        def validate(row, col):
            num = board[row][col]
            
            if num != ".":
            
                for c in range(9):
                    if board[row][c] == num and c != col:
                        return False

                for r in range(9):
                    if board[r][col] == num and r != row:
                        return False

                r = row // 3
                c = col // 3

                for i in range(r*3, r*3 + 3):
                    for j in range(c*3, c*3 + 3):
                        if board[i][j] == num and (i,j) != (row, col):
                            return False

            return True
        
        
        for r in range(9):
            for c in range(9):
                if validate(r,c) == False:
                    return False 
        
        return True 
    
        

                    
                
                
        