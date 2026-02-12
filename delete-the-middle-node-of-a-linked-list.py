class Solution:
    '''
      problem-url:- https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
    '''
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        p1=head
        p2=head
        prev=head
        while p2 != None and p2.next != None:
            p2=p2.next.next
            prev=p1
            p1=p1.next
        prev.next=p1.next
        return head
