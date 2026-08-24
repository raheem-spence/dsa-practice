class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # given: 9 x 9 sudoku board named board
        # goal: return True if valid based on conditions, else False
        # pattern: arrays and hashing?
        # approach: 

        seen_row = set()
        seen_column = set()

        # check for duplicates in row
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in seen_row:
                    return False
                else:
                    seen_row.add(board[i][j])
            seen_row.clear()

        # check for duplicates in column
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in seen_column:
                    return False
                else:
                    seen_column.add(board[j][i])
            seen_column.clear()

        seen_box = set()

        # check boxes
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] == '.':
                            continue
                        elif board[k][l] in seen_box:
                            return False
                        else:
                            seen_box.add(board[k][l])
                seen_box.clear()

        return True
            

