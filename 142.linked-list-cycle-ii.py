#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
from re import A
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
# class ListNode:

#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


# @lc code=end
a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
a.next, b.next, c.next, d.next = b, c, d, b
print(Solution().detectCycle(a).val)
