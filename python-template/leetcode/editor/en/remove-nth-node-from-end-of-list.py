#
# @lc app=leetcode id=19 lang=python3
# @lcpr version=30104
#
# [19] Remove Nth Node From End of List
#

import sys
import os

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        #删除倒数第n个，就先找到n+1节点
        p = self.FindFromEnd(dummy,n+1)
        p.next = p.next.next #跳过p的下一个节点，也就是删除p
        return dummy.next
    def FindFromEnd(self, head:Optional[ListNode], k:int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        #让 p1 走 k步
        for _ in range(k):
            p1 = p1.next
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

