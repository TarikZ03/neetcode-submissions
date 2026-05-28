class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        digit_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        rows = {}
        cols = {}
        boxes = {}

        for row in range(9):
            for col in range(9):
                row_key = row
                col_key = col
                box_key = (row // 3, col // 3)

                if row_key not in rows:
                    rows[row_key] = set()
                if col_key not in cols:
                    cols[col_key] = set()
                if box_key not in boxes:
                    boxes[box_key] = set()
                e = board[row][col]
                if e == ".":
                    continue
                e = int(e)
                if e not in digit_set or (e in rows[row_key] or e in cols[col_key] or e in boxes[box_key]):
                    return False
                rows[row_key].add(e)
                cols[col_key].add(e)
                boxes[box_key].add(e) 
                
                
        return True
