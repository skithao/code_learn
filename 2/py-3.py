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
        rtype = ListNode(0)
        p = l1
        q = l2
        curr = rtype
        carry = 0
        while p is not None or q is not None:
            x = 0 if p==None else p.val
            y = 0 if q==None else q.val
            total = carry + x + y
            carry = total/10
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            if (p is not None):
                p = p.next
            if (q is not None):
                q = q.next
        
        if(carry>0):
            curr.next = ListNode(carry)
        return rtype.next