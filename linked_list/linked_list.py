class Node:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None


# doubly linked circular list with a sentinel
class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def insert(self, *args):
        nodes = reversed([Node(arg) for arg in args])

        for x in nodes:
            x.next = self.head.next
            x.prev = self.head
            self.head.next.prev = x
            self.head.next = x

    def print(self):
        x = self.head.next

        nodes = []
        while x is not self.head:
            nodes.append(x.key)
            x = x.next
        print(nodes)

    def search(self, k):
        x = self.head.next
        while x is not self.head and x.key != k:
            x = x.next
        return x

    def delete(self, x):
        if x is not self.head:
            x.prev.next = x.next
            x.next.prev = x.prev

    def deduplication(self):
        start = self.head.next

        unique = []
        while start is not self.head:
            if start.key not in unique:
                unique.append(start.key)
            start = start.next

        new_list = LinkedList()
        new_list.insert(*unique)

        return new_list

    def merge(self, other_list):
        self.head.prev.next = other_list.head.next
        other_list.head.next.prev = self.head.prev
        self.head.prev = other_list.head.prev
        other_list.head.prev.next = self.head
        other_list.head = Node(None)

        return self


list = LinkedList()
list.insert("abc", "def", "c")
list.insert("def")
list.print()
list.delete(list.search("def"))
list.print()
list.insert("abc", "def", "bc", "bc", "c")
list.print()
list.deduplication().print()

print("")

list1 = LinkedList()
list1.insert("a", "aa", "aa", "a")
list1.print()

list2 = LinkedList()
list2.insert("b")
list2.insert("ab")
list2.insert("b")
list2.insert("c", "cc", "abc")
list2.print()

list3 = list1.merge(list2)
list3.print()
