import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        h = []
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(h,(node.val, i,node))

        dummy = ListNode()
        current = dummy
        print(h)
        while h:
            val,i,node = heapq.heappop(h)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))



        return dummy.next
