# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        hset = set()

        while curr is not None:
            if curr in hset:
                return True
            else:
                hset.add(curr)
            curr = curr.next

        return False

# date completed: July 29 2026