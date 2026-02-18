#https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while columnNumber > 0:
            if columnNumber%26 == 0:
                res = "Z" + res
                columnNumber = columnNumber//26 -1
            else:
                res = chr(columnNumber%26 + ord("A") -1) + res
                columnNumber = (columnNumber - (columnNumber%26))//26
        return res
