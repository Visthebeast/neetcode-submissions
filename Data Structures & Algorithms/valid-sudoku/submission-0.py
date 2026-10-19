import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                s = (r // 3, c // 3)

                if cell == '.':
                    continue
                
                if cell in rows[r] or cell in cols[c] or cell in squares[s]:
                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                squares[s].add(cell)
            
        return True

                
        
