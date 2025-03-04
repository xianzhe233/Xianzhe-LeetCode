#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
from typing import Optional


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:

        def list_length(head: ListNode):
            if head == None:
                return 0
            return 1 + list_length(head.next)

        len_A = list_length(headA)
        len_B = list_length(headB)
        if len_A == 0 or len_B == 0:
            return None

        if len_A >= len_B:
            pA, pB = headA, headB
        else:
            len_A, len_B = len_B, len_A
            pA, pB = headB, headA

        for _ in range(len_A - len_B):
            pA = pA.next

        while pA != None and pB != None:
            if pA == pB:
                return pA
            pA, pB = pA.next, pB.next

        return None


# @lc code=end
