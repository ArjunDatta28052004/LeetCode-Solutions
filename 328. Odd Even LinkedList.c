/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    struct ListNode* p = head;
    
    if(head==NULL){
        return NULL;
    }
    if(head->next==NULL){
        return head;
    }
    struct ListNode* q = head->next;
    struct ListNode* head2 = q;

        while(q!=NULL && q->next!=NULL){
            p->next = q->next;
            p = p->next;
            q->next = p->next;
            q=q->next;
        }
        p->next = head2;
        
    return head;
}
