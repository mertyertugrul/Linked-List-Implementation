class Node(object):
    def __init__(self, data, prev=None):
        self.value = data
        self.next = None
        self.pre = prev

class LinkedListDoubly(object):
    def __init__(self, data=None):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self, data):
        self.tail.next = Node(data, self.tail)
        self.tail = self.tail.next
        self.length += 1

    def prend(self, data):
        head_copy = self.head
        self.head = Node(data)
        self.head.next = head_copy
        self.length += 1

    def insert(self, data, index):
        if index == 0:
            self.prend(data)
            return self
        elif index + 1 > self.length:
            self.append(data)
            return self
        elif index + 1 == self.length:
            head_copy = self.head
            while head_copy.next.next is not None:
                head_copy = head_copy.next
            next_node = head_copy.next
            head_copy.next = Node(data, head_copy)
            next_node.pre = head_copy.next
            head_copy.next.next = next_node
            self.length += 1
            return self
        else:
            head_copy = self.head
            counter = 0
            while counter < index -1:
                head_copy = head_copy.next
                counter+=1
            next_node = head_copy.next
            head_copy.next = Node(data, head_copy)
            next_node.pre = head_copy.next
            head_copy.next.next = next_node
            self.length += 1

    def search(self, data):
        head_copy = self.head
        count = 0
        while head_copy is not None:
            if head_copy.value == data:
                return count
            head_copy = head_copy.next
            count += 1
        return str(data) + ' is not in the list.'

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
            head_copy.next.pre = head_copy.next
            head_copy.next = head_copy.next.next
            self.length -= 1



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
                    out += '<=> tail: ' + str(head_copy.value)
                else:
                    out += '<=> ' + str(head_copy.value)
                head_copy = head_copy.next
                i += 1
            return out


linkin = LinkedListDoubly(10)
linkin.append(20)
linkin.append(30)
linkin.append(40)
linkin.append(50)
linkin.append(60)
linkin.insert(5,3)
linkin.delete(3)
print(linkin.search(50))
print(linkin)