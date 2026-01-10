class Solution:
    """
        problem url:-  https://leetcode.com/problems/squares-of-a-sorted-array/
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        new_array = [0] * len(nums)
        for k in reversed(range(len(nums))):
            sq_i = nums[i]**2
            sq_j = nums[j]**2

            if sq_i > sq_j:
                new_array[k] = sq_i
                i += 1
            else:
                new_array[k] = sq_j
                j -= 1
        return new_array
