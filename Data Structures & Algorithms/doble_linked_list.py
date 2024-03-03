class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert(self, key, data):
        if not self.head:
            self.head = Node(data)

        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data == key:
                next = current_node.next
                current_node.next = new_node
                new_node.prev = current_node
                new_node.next = next
                if next:
                    next.prev = new_node
                    return
            else:
                current_node = current_node.next

    def delete_node(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                else:
                    next = current_node.next
                    current_node.next = None
                    next.prev = None
                    current_node = None
                    self.head = next
                    return
            elif current_node.data == key:
                if current_node.next:
                    prev = current_node.prev
                    next = current_node.next
                    prev.next = next
                    next.prev = prev
                    current_node.next = None
                    current_node.prev = None
                    current_node = prev
                    return
                else:
                    prev = current_node.prev
                    prev.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")



doubleList = DoubleLinkedList()
doubleList.append(12)
doubleList.append(40)
doubleList.append(10)
doubleList.append(60)
doubleList.display()
doubleList.delete_node(10)
doubleList.display()