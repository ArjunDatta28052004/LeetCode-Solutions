/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int pairSum(struct ListNode* head) {
    struct ListNode* p = head;
    int n = 0;
    int arr [100000];
    while(p!=NULL){
        arr[n++] = p->val;
        p = p->next;
    }
    int max = 0;
    for(int i=0;i<=(n/2)-1;i++){
        int sum = arr[i] + arr[n-1-i];
        if(sum>max){
            max = sum;
        }
    }
    return max;
}
