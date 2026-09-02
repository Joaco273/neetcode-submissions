from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue

                squareIndex = (r//3, c//3)
                if value in row[r] or value in col[c] or value in square[squareIndex]:
                    return False
                
                row[r].add(value)
                col[c].add(value)
                square[squareIndex].add(value)
                

        
        return True
    
