"""
--problem--
-----------
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

--example--
-----------
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

--link--
--------
https://leetcode.com/problems/maximum-depth-of-binary-tree/


complexity
-----------
EASY

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height)




# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n) --> axilary space since recursion

# output
"""

"""