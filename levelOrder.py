class Solution:
    '''
      problem-url:- https://leetcode.com/problems/binary-tree-level-order-traversal/
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def dfs(node,lvl):
            if node == None:
                return None
            if len(res) <= lvl:
                res.append([])
            res[lvl].append(node.val)
            dfs(node.left,lvl+1)
            dfs(node.right,lvl+1)
            return None
        dfs(root,0)
        return res
