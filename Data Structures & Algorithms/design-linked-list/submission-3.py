class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1
        
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = ListNode(val)
            self.size += 1
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        node = ListNode(val)
        node.next = cur.next
        cur.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:

            return
        
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            node = cur.next
            cur.next = cur.next.next
            node.next = None
        
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)