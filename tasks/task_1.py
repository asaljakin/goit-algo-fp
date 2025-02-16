from utils.helpers import Colors

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return
        dummy = Node(0)
        dummy.next = self.head
        last_sorted = self.head
        current = self.head.next
        while current:
            if last_sorted.data <= current.data:
                last_sorted = last_sorted.next
            else:
                prev = dummy
                while prev.next.data <= current.data:
                    prev = prev.next
                last_sorted.next = current.next
                current.next = prev.next
                prev.next = current
            current = last_sorted.next
        self.head = dummy.next

    def merge_sorted_lists(self, llist):
        p1 = self.head
        p2 = llist.head
        dummy = Node(0)
        current = dummy

        while p1 and p2:
            if p1.data <= p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        if p1:
            current.next = p1
        elif p2:
            current.next = p2

        self.head = dummy.next

    def print_list(self):
        temp = self.head
        while temp:
            end_str = " -> " if temp.next else ""
            print(f"{Colors.YELLOW}{temp.data}{Colors.RESET}{end_str}", end="")
            temp = temp.next
        print()

def task_1():
    elements = list(map(int, input(f"{Colors.BLUE}Введіть елементи списку через пробіл: {Colors.RESET}").split()))
    llist = LinkedList()
    llist.head = Node(elements[0])
    current = llist.head
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next

    print(f"{Colors.CYAN}Початковий список:{Colors.RESET}")
    llist.print_list()

    llist.reverse()
    print(f"{Colors.CYAN}Реверсований список:{Colors.RESET}")
    llist.print_list()

    llist.insertion_sort()
    print(f"{Colors.CYAN}Відсортований список:{Colors.RESET}")
    llist.print_list()

    # Створення другого відсортованого списку для прикладу об'єднання
    llist2 = LinkedList()
    elements2 = list(map(int, input(f"{Colors.BLUE}Введіть елементи другого списку через пробіл: {Colors.RESET}").split()))
    llist2.head = Node(elements2[0])
    current = llist2.head
    for element in elements2[1:]:
        current.next = Node(element)
        current = current.next

    print(f"{Colors.CYAN}Другий список:{Colors.RESET}")
    llist2.print_list()

    llist2.insertion_sort()
    print(f"{Colors.CYAN}Відсортований другий список:{Colors.RESET}")
    llist2.print_list()

    # Об'єднання двох відсортованих списків
    llist.merge_sorted_lists(llist2)
    print(f"{Colors.CYAN}Об'єднаний відсортований список:{Colors.RESET}")
    llist.print_list()

