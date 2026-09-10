class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def Push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f'"{data}" added to the stack')

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        rem = self.top.data
        self.top = self.top.next
        print(f'"{rem}" is removed from the stack')

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(f'Top element: "{self.top.data}"')

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        print("\nSTACK")
        while temp:
            print(temp.data)
            temp = temp.next



stack = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        title = input("Enter the book title: ").strip()
        if title:
            stack.Push(title)
        else:
            print("Book title cannot be empty.")

    elif choice == "2":
        stack.pop()

    elif choice == "3":
        stack.peek()

    elif choice == "4":
        stack.display()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
