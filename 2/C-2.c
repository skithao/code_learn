/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->next = NULL;
    struct ListNode* curr = dummy;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int value = carry;
        if (l1 != NULL) {
            value += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            value += l2->val;
            l2 = l2->next;
        }
        carry = value / 10;
        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        curr->next->val = value % 10;
        curr->next->next = NULL;
        curr = curr->next;
    }
    return dummy->next;
}