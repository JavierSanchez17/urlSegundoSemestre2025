class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.length += 1

    def insert_at_position(self, position, data):
        if position < 0 or position > self.length:
            return None
        if position == 0:
            self.add_to_beginning(data)
            return
        new_node = Node(data)
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1

    def remove_from_beginning(self):
        if not self.head:
            return None
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.length -= 1
        return self.head.data

    def remove_from_end(self):
        if not self.head or not self.tail:
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.length -= 1
            return data
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        data = self.tail.data
        self.tail = current_node
        self.tail.next = self.head
        self.length -= 1
        return data

    def remove_at_position(self, position):
        if position < 0 or position >= self.length:
            return None
        if position == 0:
            return self.remove_from_beginning()
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        removed_node = current_node.next
        current_node.next = current_node.next.next
        if not current_node.next:
            self.tail = current_node
        self.length -= 1
        return removed_node.data

    def remove_and_return(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_from_beginning()
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if not current_node.next:
            return None
        removed_node = current_node.next
        current_node.next = current_node.next.next
        if not current_node.next:
            self.tail = current_node
        self.length -= 1
        return removed_node.data

    def find_by_position(self, position):
        if position < 0 or position >= self.length:
            return None
        current_node = self.head
        for i in range(position):
            current_node = current_node.next
        return current_node.data

    def find(self, data):
        current_node = self.head
        if not self.head:
            return None
        if self.head.data == data:
            return self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if not current_node.next:
            return None
        return current_node.next

    def display(self):
        if not self.head:
            return None
        current_node = self.head
        result = []
        while True:
            result.append(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
        return result

    def rotate_right(self):
        if self.head is None or self.head.next is None:
            return
        self.tail = self.head
        previous_node = self.head
        current_node = self.head.next
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        self.head = current_node
        self.head.next = previous_node.next
        previous_node.next = self.head

    def rotate_left(self):
        if self.head is None or self.head.next is None:
            return
        previous_node = self.head
        current_node = self.head.next
        while current_node.next is not self.head:
            previous_node = current_node
            current_node = current_node.next
        self.tail = previous_node
        self.tail.next = self.head
        self.head = current_node
        self.head.next = None

    def print_list(self):
        """Print the elements of the circular list."""
        if not self.head:
            print("List is empty.")
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()

    def clear(self):
        """Remove all elements from the list."""
        self.head = None
        self.tail = None
        self.length = 0