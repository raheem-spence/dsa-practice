class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # given: a 9 x 9 sudoku board named board
        # goal: return true if the board is valid:
        # 1. each row must contain digits 1-9 without duplicates
        # 2. each column must contain digits 1-9 without duplicates
        # 3. each of the nine 3x3 sub boxes must contain the digits 1-9 without duplicates
        # approach: can use hashmaps for rows, columns, and boxes where the key is the coordinate for that row, column or box and the values are hashsets to store unique numbers. As we iterate over board, we check for duplicates in each of the hashsets, return false if duplicates are present else add that value to the hashsets. if we iterate over the entire board we know we have no duplicates and can return true.

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r // 3, c // 3)].add(board[r][c])
        return True