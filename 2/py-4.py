class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2 and carry == 0:
            return None
        
        value = carry
        if l1:
            value += l1.val
            l1 = l1.next
        if l2:
            value += l2.val
            l2 = l2.next
        
        carry = value // 10
        curr = ListNode(value % 10)
        curr.next = self.addTwoNumbers(l1, l2, carry)
        
        return curr
