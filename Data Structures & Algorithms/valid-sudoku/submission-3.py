class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hsh_set_row = defaultdict(set)
        hsh_set_col = defaultdict(set)
        hsh_set_grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in hsh_set_row[r] or 
                board[r][c] in hsh_set_col[c] or board[r][c] in hsh_set_grid[(r//3, c//3)]):
                    return False
                
                hsh_set_row[r].add(board[r][c])
                hsh_set_col[c].add(board[r][c])
                hsh_set_grid[(r//3, c//3)].add(board[r][c])

        return True