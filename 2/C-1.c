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

    while (l1 || l2 || carry) {
        int sum = carry + (l1? l1->val : 0) + (l2? l2->val : 0);
        carry = sum / 10;
        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        curr->next->val = sum % 10;
        curr->next->next = NULL;
        curr = curr->next;
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }

    return dummy->next;
}