class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hsh_set_row = { i : [] for i in range(9)}
    
        hsh_set_col = { i : [] for i in range(9)}
    
        squares = defaultdict(set) 
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val != ".":
                    val = int(val)
                    if val in hsh_set_row[i] or val in hsh_set_col[j] or val in squares[(i // 3, j // 3)]:
                        return False
                    
                    else : 
                        hsh_set_row[i].append(val)
                        hsh_set_col[j].append(val)
                        squares[(i // 3, j // 3)].add(val)
    
    
        return True