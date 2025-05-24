#
# @lc app=leetcode id=378 lang=python3
# @lcpr version=30201
#
# [378] Kth Smallest Element in a Sorted Matrix
#

from queue import PriorityQueue
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = PriorityQueue() #创建一个优先级队列
        #要放入队列的项。通常是一个元组，格式为 (priority, data)，
        # 其中 priority 是数字，数值越小优先级越高。
        #初始化优先级队列，将每一行的第一个元素装进去
        print(len(matrix))
        for i in range(len(matrix)):
            pq.put((matrix[i][0],i,0)) 
            '''
            matrix[i][0]: 第 i 行的第一个值，作为 优先级排序的依据。

            i: 表示这个值来自第几行。

            0: 表示这个值是该行的第几列（初始都是第 0 列）。

            所以你等于往队列中放入一个三元组 (值, 行号, 列号)。
            matrix = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
            ]

            此时 pq中存入的就是 （1，0，0）、（2，1，0）;(3,2,0)
            '''
            
        res = -1
        #     # 执行合并多个有序链表的逻辑，找到第 k 小的元素
        while not pq.empty() and k > 0:
            cur = pq.get() # 取出并得到pd中优先级最高的元素，也就是“最小”的那个，优先级按元组中第一个值来判断
            res = cur[0] #第一次执行 得到1
            k -= 1
            #链表中的下一个节点加入优先级
            i,j = cur[1],cur[2] #第一次执行 i = 0, j = 0
            if j+1 < len(matrix[i]):
                pq.put((matrix[i][j + 1], i, j + 1))
            #此时 pd 里存入的是
            #(2,1,0);(3,2,0);(4,0,1                                                                                                                                                                               )
            return res #当k = 0 时，按照顺序取出的就是第k个最小的元素

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [[1,5,9],[10,11,13],[12,13,15]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[-5]]\n1\n
# @lcpr case=end

#

