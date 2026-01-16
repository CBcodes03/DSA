class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #using floyds slow fast pointer
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast == slow:
                return True
        return False
