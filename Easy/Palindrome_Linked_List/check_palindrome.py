from linked_list import linkedList


def list_to_llist(test_list: list):
    llist = linkedList()
    for var in test_list:
        llist.insertAtEnd(var)
    return llist


list_1 = [1, 2, 2, 1]
llist_1 = list_to_llist(list_1)

list_2 = [1, 2, 3, 4]
llist_2 = list_to_llist(list_2)

# thats how the llist looks like
# print(llist_2)
# print(llist_2.head.next.val)
# print(llist_2.head.val)


# shorter version
def check_palindrome_2(test_list):
    string, head = "", test_list.head
    while head:
        string += str(head.val)
        head = head.next
    if string == string[::-1]:
        return True
    return False


# longer version
def check_palindrome(test_list):
    # turning all values into string
    #  print(test_list) # for checking
    string = ''
    head = test_list.head
    while (head != None):
        string += str(head.val)
        head = head.next

    # checking if first and back in each iter. is the same
    n = len(string)
    for i in range(int(n/2)):
        #  print(string[i]) # for checking
        #  print(string[int(n-i-1)]) # fro checking
        if (string[i] != string[n-i-1]):
            return False
    return True


print('######')
print(check_palindrome(llist_2))
print(check_palindrome(llist_1))
print('######')
print(check_palindrome_2(llist_2))
print(check_palindrome_2(llist_1))
