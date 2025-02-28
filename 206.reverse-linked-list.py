#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListRecursive(head)


    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, current, next = None, head, None
        while True:
            if current == None:
                return pre
            next = current.next
            current.next = pre
            pre = current
            current = next
            
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head, last):
            if head.next == None:
                new_head = head
            else:   
                new_head = reverse(head.next, head)
            head.next = last
            return new_head
        
        if head == None:
            return head
        return reverse(head, None)

        
# @lc code=end

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = Solution().reverseList(head)
while reversed_head != None:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next