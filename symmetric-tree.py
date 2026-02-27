#https://leetcode.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node1,node2):
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            if node1.val == node2.val:
                return helper(node1.left,node2.right) and helper(node1.right,node2.left)
            else:
                return False
        return helper(root.left,root.right)
