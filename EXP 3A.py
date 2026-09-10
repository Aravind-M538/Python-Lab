Max = 100
stack = []

def push():
    if len(stack) >= Max:
        print("stack overflow")
    else:
        book = input("Enter book title to push: ")
        stack.append(book)
        print(book, "added to stack")

def pop():
    if len(stack) == 0:
        print("stack underflow")
    else:
        book = stack.pop()
        print(book, "removed from stack")

def display():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("Book in stack:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

n = int(input("Enter number of books: "))
for i in range(n):
    push()

print("In stack after push:")
display()

choice = int(input("\nEnter choice (1-push, 2-pop): "))
if choice == 1:
    push()
elif choice == 2:
    pop()
else:
    print("Invalid choice")

print("\nFinal stack:")
display()
