#
# @lc app=leetcode id=142 lang=python3
# @lcpr version=30200
#
# [142] Linked List Cycle II
#

from asyncio.windows_events import NULL
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #第一步参考141题，通过快慢指针的方法找到相交点
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        
        
        if fast == None or fast.next == None:
            return None
        slow = head
        while fast != slow:
            slow= slow.next
            fast = fast.next
        return slow
    
        
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

