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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null){
            return false;
        }
        if(targetSum == root.val && root.left == null && root.right == null){
            return true;
        }
        return hasPathSum(root.left,targetSum,root.val) || hasPathSum(root.right,targetSum,root.val);
    }
    public boolean hasPathSum(TreeNode root, int targetSum,int currentSum) {
        if (root == null){
            return false;
        }
        if (root.left != null || root.right != null){
            currentSum+=root.val;
            return hasPathSum(root.left,targetSum,currentSum) || hasPathSum(root.right,targetSum,currentSum);
        }else{
            if(currentSum+root.val == targetSum){
                return true;
            }
        }
        return false;
    }
}