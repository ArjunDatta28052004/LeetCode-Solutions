/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if(root==NULL){
        return 0;
    }
    int lheight = maxDepth(root->left);
    int rheight = maxDepth(root->right);

    return (lheight>rheight?lheight:rheight)+1;
}
