#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class Node:
    def __init__(self, val, pre=None, next=None) -> None:
        self.val = val
        self.pre = pre
        self.next = next

class MyLinkedList:

    def __init__(self):
        sentinel = Node("SENTINEL")
        sentinel.pre = sentinel
        sentinel.next = sentinel
        self.head = sentinel
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        p = self.head.next
        for _ in range(index):
            p = p.next
        
        return p.val
        

    def addAtHead(self, val: int) -> None:
        pre = self.head
        next = self.head.next
        p = Node(val, pre, next)
        pre.next = p
        next.pre = p
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        pre = self.head.pre
        next = self.head
        p = Node(val, pre, next)
        pre.next = p
        next.pre = p
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        pre = self.head
        for _ in range(index):
            pre = pre.next
            
        next = pre.next
        p = Node(val, pre, next)
        pre.next = p
        next.pre = p
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        pre = self.head
        for _ in range(index):
            pre = pre.next
        del_node = pre.next
        next = del_node.next
        pre.next = next
        next.pre = pre
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

