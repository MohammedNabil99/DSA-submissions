# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        # current = head
        # length = 0

        # while current:
        #     length += 1
        #     current = current.next
        
        # temp_head = ListNode(0, head)
        # prev = temp_head
        # steps_to_target = length - n

        # for _ in range(steps_to_target):
        #     prev = prev.next
        
        # prev.next = prev.next.next
        
        # return temp_head.next

        temp_head = ListNode(0, head)

        slow = fast = temp_head

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return temp_head.next



        