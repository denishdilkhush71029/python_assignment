import numpy as np

print("1. Ones 2. Max/Min 3. Dot Product 4. Reshape")
choice = input("Choice: ")

if choice == '1':
    print(np.ones((3,3)))
elif choice == '2':
    arr = np.array([10, 20, 5, 40])
    print(f"Max: {arr.max()}, Min: {arr.min()}")
elif choice == '3':
    a, b = np.array([1, 2]), np.array([3, 4])
    print("Dot Product:", np.dot(a, b))
elif choice == '4':
    arr = np.arange(6)
    print("Reshaped:\n", arr.reshape(2, 3))
    