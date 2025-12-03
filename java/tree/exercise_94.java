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
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root == null){
            List<Integer> rootList = new ArrayList<>();
            return rootList;      
        }
        if(root.left == null && root.right == null){
            List<Integer> rootList = new ArrayList<>();
            rootList.add(root.val);
            return rootList;
        }
        List<Integer> left = inorderTraversal(root.left);
        List<Integer> right = inorderTraversal(root.right);
        left.add(root.val);
        left.addAll(right);
        return left;
    }
}