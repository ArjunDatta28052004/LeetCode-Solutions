/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* searchBST(struct TreeNode* root, int val) {

    if(root==NULL){
        return NULL;
    }
    if(root->val==val){
        return root;
    }
    struct TreeNode* p = NULL;
    if(root->val<val){
        p = searchBST(root->right, val);
    }
    else{
        p = searchBST(root->left, val);
    }

    return p;
    
}
