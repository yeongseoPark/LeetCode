class Solution(object):
    def searchMatrix(self, matrix, target):
        
        r, c = len(matrix), len(matrix[0])
        low, high = 0, r * c - 1
        
        while low <= high:
            mid = (low+high) // 2
            num = matrix[mid//c][mid%c]
            
            if num == target:
                return True 
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False