"""
LeetCode 706 - Design HashMap

Difficulty: Easy

Time Complexity:
- put: O(1) average, O(n) during resize
- get: O(1) average
- remove: O(1) average

Space Complexity: O(n)

Technique:
- Separate Chaining
"""

class DoublyNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, item):
        node = DoublyNode(item)

        if self.head is None:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def delete(self, key):
        current = self.head

        while current:
            if current.item[0] == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return True
            current = current.next

        return False


class MyHashMap:
    MAX_LOAD_FACTOR = 0.75

    def __init__(self):
        self.elements = [DoublyLinkedList()]
        self.__size = 0
        self.__capacity = 1

    def hash(self, key):
        total = key * 31
        return total

    def _get_index(self, key_value):
        return key_value % self.__capacity

    def _hash_get_index(self, key):
        key_value = self.hash(key)
        return self._get_index(key_value)

    def _resize(self):
        old_elements = self.elements
        old_capacity = self.__capacity
        self.__capacity *= 2
        self.elements = [DoublyLinkedList() for _ in range(self.__capacity)]

        for i in range(old_capacity):
            current = old_elements[i].head

            while current:
                index = self._hash_get_index(current.item[0])
                self.elements[index].prepend((current.item[0], current.item[1]))
                current = current.next

    def update_existing_key(self, key, value):
        # hash and get index
        index = self._hash_get_index(key)

        # check if key exists:
        current = self.elements[index].head
        while current:
            if current.item[0] == key:
                current.item = (key, value)
                return True

            current = current.next
        return False

    def put(self, key: int, value: int) -> None:
        if value is None:
            raise ValueError("Invalid None value")

        if self.update_existing_key(key, value) is True:
            return

        index = self._hash_get_index(key)

        # check for load factor and do resize and rehash when neccessary
        if (self.__size + 1) / self.__capacity > self.MAX_LOAD_FACTOR:
            self._resize()
            index = self._hash_get_index(key)

        # insert
        self.elements[index].prepend((key, value))

        # size, capacity, load factor
        self.__size += 1

    def get(self, key: int) -> int:
        index = self._hash_get_index(key)
        current = self.elements[index].head

        while current:
            if current.item[0] == key:
                return current.item[1]
            current = current.next

        return -1

    def remove(self, key: int) -> None:
        index = self._hash_get_index(key)

        self.elements[index].delete(key)
        if self.elements[index].delete(key):
            self.__size -= 1


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(50, "value")
print(obj.elements[0].head.item)
param_2 = obj.get(50)
print(param_2)
obj.remove(50)
