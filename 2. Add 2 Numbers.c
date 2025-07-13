struct ListNode* createNode(int val){
    struct ListNode* new = malloc(sizeof(*new));
    new->val = val;
    new->next = NULL;
    return new;
}


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

    struct ListNode* p = l1;
    struct ListNode* q = l2;
    struct ListNode* new = malloc(sizeof(*new));
    struct ListNode* x = new;
    int carry = 0;
    while(p!=NULL || q!=NULL || carry){
        int sum = carry;
        if(p){
            sum += p->val;
            p = p->next;
        }
        if(q){
            sum += q->val;
            q = q->next;
        }
        carry = sum/10;
        x->next = createNode(sum%10);
        x = x->next;
    }
    return new->next;

    
}
