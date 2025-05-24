#
# @lc app=leetcode id=373 lang=python3
# @lcpr version=30201
#
# [373] Find K Pairs with Smallest Sums
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from queue import PriorityQueue
# @lc code=start
class Solution1:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #[1,7,11];[2,4,6]
        pq = PriorityQueue()
        # 存储4元组 (sum, num1[i], nums2[i], i)
        # i 记录 nums2 元素的索引位置，用于生成下一个节点
        for i in range(len(nums1)):
            pq.put((nums1[i]+nums2[0],nums1[i],nums2[0],0))
            #pq = (3,1,2,0)(9,7,2,0)(13,11,2,0) zui
        res = []

        while not pq.empty() and k > 0 :
            _, num1,num2,idx = pq.get()
            k -= 1
            next_index = idx + 1
            if next_index < len(nums2):
                pq.put((num1+nums2[next_index],num1,nums2[next_index],next_index))
            pair = [num1,num2]
            res.append(pair)

        return res 
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        res = []

        # 初始化：将每个 nums1[i] 与 nums2[0] 的组合加入堆
        for i in range(min(k, len(nums1))):
            # 存储格式为：(pair_sum, index_in_nums1, index_in_nums2)
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        # 从堆中取出最小的 k 个数对
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                # 推进 nums2 的索引，构造新的候选对
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#

