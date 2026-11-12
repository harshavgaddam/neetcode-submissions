class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        boxes=defaultdict(set)
        for r in range(9):
            for c in range(9):
                number=board[r][c]
                if number == ".":
                    continue
                box=(r//3,c//3)
                if(number in rows[r] or number in cols[c] or number in boxes[box]):
                    return False
                rows[r].add(number)
                cols[c].add(number)
                boxes[box].add(number)
        return True