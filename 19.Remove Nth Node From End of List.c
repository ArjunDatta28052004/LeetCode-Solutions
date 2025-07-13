struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* p = head;
    

    int counter = 0;
    if(p!=NULL){
        counter=1;
        while(p->next!=NULL){
            p = p->next;
            counter += 1;
        }
    }
    if(n<=counter){
        struct ListNode* q = head;
        struct ListNode* r=NULL;
        int x = 0;
        if(q!=NULL){
            x = 1;
            while(x!=(counter-n)+1 && q->next!=NULL){
                r = q;
                q = q->next;
                x++;
            }
            if(q==head && q->next==NULL){
                free(head);
                return NULL;
            }
            else if(q==head && q->next!=NULL){
                if(n==counter){
                    struct ListNode* new_head = head->next;
                    free(head);
                    return new_head;
                }
                else{
                    r = q;
                    q = q->next;
                    r->next = q->next;
                    free(q);
                    return head;
                }
                
            }
            else{
                r->next = q->next;
                free(q);
                return head;
            }
            
        }
    }
    
    return 0;
    
}
