# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow
        prev=None

        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt    

        res=0
        first,second=head,prev
        while second:
            res=max(res,first.val+second.val)
            first=first.next
            second=second.next

        return res

        
        