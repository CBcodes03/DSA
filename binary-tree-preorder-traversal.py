class Solution:
  '''
    problem:- https://leetcode.com/problems/binary-tree-preorder-traversal/
  '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(node):
            if node:
                res.append(node.val)
            else:
                return None
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return res
