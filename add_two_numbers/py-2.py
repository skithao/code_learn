# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = dummy = ListNode(0)
        carry = 0
        l1_state = l1
        l2_state = l2

        while l1_state or l2_state or carry:
            value = carry + (l1_state.val if l1_state is not None else 0) + (l2_state.val if l2_state is not None else 0)
            carry = value // 10
            val = value % 10

            current.next = ListNode(val)
            current = current.next
            
            if l1_state is not None: l1_state = l1_state.next
            if l2_state is not None: l2_state = l2_state.next
        
        return dummy.next