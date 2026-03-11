def find_indices(s1, s2):
    indices = []
    start = 0
    while True:
        start = s1.find(s2, start)
        if start == -1: break
        indices.append(start)
        start += 1
    return indices if indices else -1

str1 = input("Enter main string: ")
str2 = input("Enter substring: ")
print("Indices:", find_indices(str1, str2))