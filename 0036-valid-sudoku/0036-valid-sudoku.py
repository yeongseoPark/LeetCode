class Solution(object):
    def isValidSudoku(self, board):
        dupl_set = set()
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if (str(num) + " in row " + str(i)) in dupl_set:
                        return False
                    dupl_set.add(str(num) + " in row " + str(i))
                    
                    if (str(num) + " in col " + str(j)) in dupl_set:
                        return False
                    
                    dupl_set.add(str(num) + " in col " + str(j))
                    
                    if (str(num) + "in box " + str(i // 3) + str(j // 3)) in dupl_set:
                        return False
                    
                    dupl_set.add(str(num) + "in box " + str(i // 3) + str(j // 3))
        return True
        

                    
                
                
        