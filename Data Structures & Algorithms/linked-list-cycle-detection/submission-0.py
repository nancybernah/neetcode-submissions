# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        curr = head
        hmap = {}
        index = 0
        while curr.next != None:
            if curr.val in hmap:
                return True

            hmap[curr.val] = index
            curr = curr.next
            index +=1
        return False
