class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(curr, open_cnt, close_cnt):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if open_cnt < n:
                helper(curr + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                helper(curr + ")", open_cnt, close_cnt + 1)

        helper("", 0, 0)
        return res