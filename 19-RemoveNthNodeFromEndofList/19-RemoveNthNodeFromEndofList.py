        start->next = head;
        ListNode* slow = start;
        ListNode* fast = start;
        for(int i = 0; i < n; ++i) {
            fast = fast->next;
        }
        while(fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* start = new ListNode();
public:
class Solution {
[1,2,3,4,5]
