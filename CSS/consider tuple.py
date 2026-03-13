t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Split and print
mid = len(t1) // 2
print(t1[:mid])
print(t1[mid:])

# b. Even values to t2
t2 = tuple(x for x in t1 if x % 2 == 0)
print("t2 (even):", t2)

# c. Concatenate
t3 = (11, 13, 15)
print("Concatenated:", t1 + t3)

# d. Max/Min
print(f"Max: {max(t1)}, Min: {min(t1)}")
