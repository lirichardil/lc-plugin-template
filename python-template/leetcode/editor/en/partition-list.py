#
# @lc app=leetcode id=86 lang=python3
# @lcpr version=30104
#
# [86] Partition List
#

import sys
import os

from networkx import null_graph

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
       dummy1 = ListNode(-1)
       dummy2 = ListNode(-1)
       p1,p2 = dummy1,dummy2
       p = head 
       while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            temp = p
            p.next = None
            p = temp

        p1.next = dummy2.next
       
        return dummy1.next
           

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    L = ListNode.create_head([1,4,5,22,34,7])
    res = solution.partition(L,7)
    ListNode.print(res)
#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

