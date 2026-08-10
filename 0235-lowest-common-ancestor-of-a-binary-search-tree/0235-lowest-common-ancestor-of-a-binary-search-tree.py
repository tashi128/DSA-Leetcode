class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            # both nodes are smaller, LCA must be on the left
            if p.val < root.val and q.val < root.val:
                root = root.left

            # both nodes are larger, LCA must be on the right
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # they split, or root itself is p/q
            else:
                return root