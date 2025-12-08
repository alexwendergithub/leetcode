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

    public List<Integer> postorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> traversalStack = new ArrayDeque<>();
        TreeNode currentNode = root;

        while (currentNode != null || !traversalStack.isEmpty()) {
            if (currentNode != null) {
                result.add(currentNode.val);
                traversalStack.push(currentNode);
                currentNode = currentNode.right;
            } else {
                currentNode = traversalStack.pop();
                currentNode = currentNode.left;
            }
        }

        Collections.reverse(result);
        return result;
    }
}