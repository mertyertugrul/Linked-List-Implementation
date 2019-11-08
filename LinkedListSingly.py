class Node(object):
    def __init__(self, data=None, ):
        self.value = data
        self.next = None


class LinkedListSingly(object):
    def __init__(self, data=None):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.length += 1
        return self

    def prenend(self, data):
        head_copy = self.head
        self.head = Node(data)
        self.head.next = head_copy
        self.length += 1
        return self

    def search(self, data):
        head_copy = self.head
        count = 0
        while head_copy is not None:
            if head_copy.value == data:
                return count
            head_copy = head_copy.next
            count += 1
        return str(data) + ' is not in the list.'

    def insert(self, data, index):
        if index == 0:
            self.prenend(data)
            return self
        elif index + 1 > self.length:
            self.append(data)
            return self
        elif index + 1 == self.length:
            head_copy = self.head
            while head_copy.next.next is not None:
                head_copy = head_copy.next
            next_node = head_copy.next
            head_copy.next = Node(data)
            head_copy.next.next = next_node
            self.length += 1
            return self
        else:
            count = 0
            head_copy = self.head
            while count < index - 1:
                head_copy = head_copy.next
                count += 1
            next_node = head_copy.next
            head_copy.next = Node(data)
            head_copy.next.next = next_node
            self.length += 1
            return self

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        elif index + 1 == self.length:
            head_copy = self.head
            while head_copy.next.next is not None:
                head_copy = head_copy.next
            head_copy.next = None
            self.length -= 1
        else:
            head_copy = self.head
            count = 0
            while count != index - 1:
                head_copy = head_copy.next
                count += 1
            head_copy.next = head_copy.next.next
            self.length -= 1

    def reverse(self):
        first = self.head
        second = self.head.next
        self.tail = self.head

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

    def __str__(self):
        out = ''
        if self.length < 1:
            out = 'This list has no values.'
        else:
            i = 0
            head_copy = self.head
            while head_copy is not None:
                if i == 0:
                    out = 'head: ' + str(head_copy.value)
                elif i == self.length - 1:
                    out += '=> tail: ' + str(head_copy.value)
                else:
                    out += '=> ' + str(head_copy.value)
                head_copy = head_copy.next
                i += 1
        return out


linkin = LinkedListSingly(10)
linkin.append(20)
linkin.append(30)
linkin.append(40)
linkin.append(50)
linkin.append(60)
linkin.delete(3)
linkin.reverse()
print(linkin.search(20))
print(linkin)
# linkin.prenend(5)
# print(linkin)


