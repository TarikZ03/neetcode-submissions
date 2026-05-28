class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        digit_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        for r in board:
            row_duplicate_set = set()
            for e in r:
                if e == ".":
                    continue
                e = int(e)
                if e not in digit_set or e in row_duplicate_set:
                    return False
                row_duplicate_set.add(e)

        for col in range(9):
            col_duplicate_set = set()
            for row in range(9):
                e = board[row][col]
                if e == ".":
                    continue
                e = int(e)
                if e not in digit_set or e in col_duplicate_set:
                    return False
                col_duplicate_set.add(e)

        boxes = {}

        for row in range(9):
            for col in range(9):
                box_key = (row // 3, col // 3)
                if box_key not in boxes:
                    boxes[box_key] = set()
                e = board[row][col]
                if e == ".":
                    continue
                e = int(e)
                if e not in digit_set or e in boxes[box_key]:
                    return False
                boxes[box_key].add(e) 
                
                
        return True
