class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        sub_boxes = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):

                digit = board[i][j]
                
                if digit == ".":
                    continue
                
                sub_index = i // 3 * 3 + j // 3
                
                rows[i].append(digit)
                columns[j].append(digit)
                sub_boxes[sub_index].append(digit)
        
        for val in rows + columns + sub_boxes:
            if len(val) != len(set(val)):
                return False
        
        return True