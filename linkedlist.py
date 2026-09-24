class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise ValueError("Position cannot be negative")

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0

        while current is not None and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Position is out of range")

        new_node.next = current.next
        current.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            raise IndexError("List is empty")

        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            raise IndexError("List is empty")

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_by_value(self, value):
        if self.head is None:
            raise ValueError("Value not found in empty list")

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

        raise ValueError(f"Value {value} not found")

    def search(self, value):
        current = self.head
        position = 0

        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1

        return -1

    def display(self):
        current = self.head
        if current is None:
            print("Linked list is empty")
            return

        values = []
        while current is not None:
            values.append(str(current.data))
            current = current.next

        print(" -> ".join(values))


if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_position(15, 2)

    print("Current list:")
    linked_list.display()

    print("Search for 15 ->", linked_list.search(15))

    linked_list.delete_by_value(20)
    print("After deleting 20:")
    linked_list.display()
