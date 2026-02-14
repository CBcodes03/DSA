class Solution:
    '''
      url:- https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
    '''
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node :
                return None
            ltail = dfs(node.left)
            rtail = dfs(node.right)

            if ltail:
                ltail.right = node.right
                node.right = node.left
                node.left = None
            
            return rtail or ltail or node

        dfs(root)
        return None
