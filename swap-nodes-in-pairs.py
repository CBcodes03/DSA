#https://leetcode.com/problems/swap-nodes-in-pairs/
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(f,s):
            if f != None and s != None:
                f.next = s.next
                s.next = f
                if f.next!=None:
                    f.next = helper(f.next,f.next.next)
                    return s
                else:
                    return s
            else:
                return f
        if head!= None and head.next!= None:
            return helper(head,head.next)
        return head
