/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isSymmetrical(root.left,root.right);
    }
    public boolean isSymmetrical(TreeNode p, TreeNode q) {
        if(p == null && q != null){
            return false;
        }
        if(q == null && p != null){
            return false;
        }
        if(p == null && q == null){
            return true;
        }
        return p.val == q.val && isSymmetrical(p.left,q.right) && isSymmetrical(p.right,q.left);
    }
}