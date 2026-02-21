# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy  = ListNode(0,head)
        current = dummy
        i = 0
        for 
        while i!=k:
            if i==k-1:
                current = current.next
            elif i==k:
