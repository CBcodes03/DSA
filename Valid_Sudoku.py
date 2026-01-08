class Solution:
    """
    problem_url:- https://leetcode.com/problems/valid-sudoku/description/
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for row in range(len(board)):
            for column in range(len(board)):
                box=(row//3 , column//3)
                if board[row][column] != '.':
                    if (board[row][column],"box",box) in seen:
                        return False
                    else:
                        seen.add((board[row][column],"box",box))
                    if (board[row][column],"row",row) in seen:
                        return False
                    else:
                        seen.add((board[row][column],"row",row))
                    if (board[row][column],"column",column) in seen:
                        return False
                    else:
                        seen.add((board[row][column],"column",column))
        return True
