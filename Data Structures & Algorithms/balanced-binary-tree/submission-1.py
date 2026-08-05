# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        depths = {None: 0}
        curr = root
        last_visited = None

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                if peek.right and last_visited != peek.right:
                    curr = peek.right
                else:
                    node = stack.pop()
                    left_h = depths[node.left]
                    right_h = depths[node.right]

                    if abs(left_h - right_h) > 1:
                        return False

                    depths[node] = 1 + max(left_h, right_h)
                    last_visited = node
        return True
