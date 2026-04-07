s = input("Enter a string: ")
print("1. Frequency 2. Replace 3. Remove First 4. Remove All")
choice = input("Select operation: ")

if choice == '1':
    char = input("Enter character: ")
    print("Frequency:", s.count(char))
elif choice == '2':
    old, new = input("Old char: "), input("New char: ")
    print("Result:", s.replace(old, new))
elif choice == '3':
    char = input("Enter character to remove: ")
    print("Result:", s.replace(char, "", 1))
elif choice == '4':
    char = input("Enter character to remove: ")
    print("Result:", s.replace(char, ""))
