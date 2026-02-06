class Solution:
    '''
    problem:- https://leetcode.com/problems/same-tree/
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(r1,r2):
            if (r1 != None and r2 != None) and r1.val == r2.val:
                if r1.left != None and r2.left != None:
                    l=traverse(r1.left,r2.left)
                else:
                    if r1.left == r2.left:
                        l=True
                    else: 
                        return False
                if r1.right != None and r2.right != None:
                    r=traverse(r1.right,r2.right)
                else:
                    if r1.right == r2.right:
                        r=True
                    else:
                        return False
                return l and r
            else:
                if r1 == None and r2 == None:
                    return True
                return False
        return traverse(p,q)
