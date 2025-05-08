#
# @lc app=leetcode id=141 lang=python3
# @lcpr version=30104
#
# [141] Linked List Cycle
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            
        return False
                
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

