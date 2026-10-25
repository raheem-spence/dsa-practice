class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use dicts where the keys correspond to each row, column or 3x3 box respectively and the values are sets to ensure uniqueness for each
        # scan the board to see for empty spaces i.e. '.' and continue else check for duplicates in each row, column, or box. if duplicates return false, else return true
        # the trick is that each 3x3 box can be represented by (r // 3, c // 3) so theres (0,0) box, (1, 0) box, etc. so if we're on row 0, col 0 we get (0 // 3, 0 // 3) which evaluates to (0, 0) which is the box we are on. note, // is integer (floor) division

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r // 3, c // 3)].add(board[r][c])
        return True
