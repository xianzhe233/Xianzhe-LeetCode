#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = head
        for i in range(n):
            if p2 == None:
                return head
            p2 = p2.next
        
        if p2 == None:
            return head.next

        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        next = p1.next
        p1.next = next.next
        del next
        
        return head
# @lc code=end

