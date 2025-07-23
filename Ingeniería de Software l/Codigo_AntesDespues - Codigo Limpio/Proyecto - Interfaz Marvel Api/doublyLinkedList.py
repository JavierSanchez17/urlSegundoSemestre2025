class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def add_to_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def add_at_position(self, data, position):
        if position < 0 or position > self.length:
            raise IndexError("Position out of range")
        if position == 0:
            self.add_to_start(data)
        elif position == self.length:
            self.add_to_end(data)
        else:
            new_node = Node(data)
            current_node = self.get_node(position - 1)
            new_node.next = current_node.next
            new_node.prev = current_node
            if current_node.next is not None:
                current_node.next.prev = new_node
            else:
                self.tail = new_node
            current_node.next = new_node
            self.length += 1

    def remove_from_start(self):
        if self.head is None:
            raise IndexError("List is empty")
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return data

    def remove_from_end(self):
        if self.tail is None:
            raise IndexError("List is empty")
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return data

    def remove_at_position(self, position):
        if position < 0 or position >= self.length:
            raise IndexError("Position out of range")
        if position == 0:
            self.remove_from_start()
        else:
            current_node = self.get_node(position - 1)
            data = current_node.next.data
            current_node.next = current_node.next.next
            if current_node.next is not None:
                current_node.next.prev = current_node
            else:
                self.tail = current_node
            self.length -= 1
            return data

    def remove_by_data(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                self.length -= 1
                return True
            current_node = current_node.next
        return False

    def search_by_position(self, position):
        if position < 0 or position >= self.length:
            raise IndexError("Position out of range")
        return self.get_node(position)

    def search_by_data(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def rotate_right(self):
        if self.length < 2:
            return
        self.tail, self.head = self.head, self.tail
        self.tail.next = None
        self.head.prev = None
        current_node = self.head
        for _ in range(self.length - 1):
            next_node = current_node.next
            current_node.next = current_node.prev
            current_node.prev = next_node
            current_node.prev.next = current_node
            current_node.next.prev = current_node
            current_node = next_node
        self.tail = current_node
        self.tail.next = None

    def rotate_left(self):
        if self.length < 2:
            return
        self.tail, self.head = self.head, self.tail
        self.head.prev = None
        current_node = self.head
        for _ in range(self.length - 1):
            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node
            current_node.next.prev = current_node
            current_node.prev.next = current_node
            current_node = prev_node
        self.head = current_node
        self.head.prev = None

    def get_node(self, position):
        if position < 0 or position >= self.length:
            raise IndexError("Position out of range")
        if position < self.length // 2:
            current_node = self.head
            for _ in range(position):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - position - 1):
                current_node = current_node.prev
        return current_node

    def print_list(list):
        current_node = list.head
        while current_node is not None:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
