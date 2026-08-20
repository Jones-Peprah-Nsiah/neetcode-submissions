# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        curr=slow
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        res=0
        first,second=head,prev
        while second:

            res=max(res,first.val+second.val)
            first=first.next
            second=second.next
        return res

            
        