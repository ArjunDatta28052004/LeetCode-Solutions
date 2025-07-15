/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode* p =head;
    int counter = 0;
    if(head==NULL){
        return NULL;
    }
    else if(head->next==NULL){
        free(head);
        return NULL;
    }
    else{
        while(p->next!=NULL){
            p=p->next;
            counter++;
        }
        int mid;
        if(counter%2==0){
            mid = counter/2;
        }
        else{
            mid = (counter/2)+1;
        }

        int itr = 0;
        struct ListNode* q=head;
        struct ListNode* r = NULL;

        while(q->next!=NULL && itr<mid){
            r = q;
            q=q->next;
            itr++;
        }
        r->next = q->next;
        free(q);
        }
    

        return head;

    
}
