#
# @lc app=leetcode id=21 lang=python3
# @lcpr version=30104
#
# [21] Merge Two Sorted Lists
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from tkinter import N
from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        p1,p2 = list1,list2

        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p.next = p1
                
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        
        if p1 is not None:
            p.next = p1
        
        if p2 is not None:
            p.next = p2
        return dummy.next

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

