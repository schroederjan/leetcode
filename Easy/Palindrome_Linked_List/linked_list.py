""" module for custom linked list class """


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        """ to print out linked list like normal list """
        result = ""
        pointer = self.head
        while pointer:
            result += f"{str(pointer.val)}, "
            pointer = pointer.next
        result = result.strip(", ")
        if len(result):
            return f"[{result}]"
        else:
            return "[]"

    def insertAtBeginning(self, val):
        temp = Node(val)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def insertAtEnd(self, val):
        temp = Node(val)
        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = temp


if __name__ == '__main__':

    llist = linkedList()
    values = [1, 2, 2, 1]
    #values = [1, 2, 3, 4]

    for v in values:
        llist.insertAtBeginning(val=v)
        # llist.insertAtEnd(val=v)

    print(llist)
