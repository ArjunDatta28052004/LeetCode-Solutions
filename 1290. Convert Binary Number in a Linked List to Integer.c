/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <math.h>
int getDecimalValue(struct ListNode* head) {
    if(head==NULL){
        return 0;
    }
    else if(head->next==NULL){
        return head->val;
    }
    else{
        int counter = 0;
        struct ListNode* p = head;
        while(p->next!=NULL){
            if(counter==0 && p->val==0){
                p=p->next;
            }
            else{
                p=p->next;
                counter++;
            }
        }
        struct ListNode* q = head;
        while(q->val==0 && q->next!=NULL){
            q=q->next;
        }
        int decimal=0;
        for(int i=counter;i>=0;i--){
            decimal += ((q->val)*pow(2,i));
            q=q->next;
        }
        return decimal;

    }
    
    
}
