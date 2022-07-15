"""
--problem--
-----------
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

--example--
-----------
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Example 2:

Input: preorder = [1,3]
Output: [1,null,3]


--Constraints--
---------------
1 <= preorder.length <= 100
1 <= preorder[i] <= 1000
All the values of preorder are unique.


--link--
--------
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/


complexity
-----------
MEDIUM

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    def bstFromPreorder(self, preorder):
        return self.build_tree(preorder, sys.maxsize, [0])
    def build_tree(self, preorder, upper_bound, ind):
        if ind[0] == len(preorder)  or preorder[ind[0]] > upper_bound:
            return None
        root = TreeNode(preorder[ind[0]])
        ind[0] +=1
        root.left = self.build_tree(preorder, root.val, ind)
        root.right = self.build_tree(preorder, upper_bound, ind)
        return root



# time and space complexity
# -------------------------
# time --> O(n)
# space -> O(n)[axilory]

# output
"""

"""