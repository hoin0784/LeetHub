class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        top, bottom = 0, len(matrix)-1                      # top = 0, bottom = 2

        while top <= bottom:            
            mid = (top + bottom) // 2

            if matrix[mid][0] > target:
                bottom = mid - 1 
            
            elif matrix[mid][-1] < target:
                top = mid + 1
            
            else:
                break

        row = (top + bottom) // 2

        left ,right = 0, len(matrix[row])-1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False


      
            


        