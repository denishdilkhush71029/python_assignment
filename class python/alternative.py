def copy_odd_lines(source, dest):
    with open(source, 'r') as f1, open(dest, 'w') as f2:
        for i, line in enumerate(f1, 1):
            if i % 2 != 0:
                f2.write(line)

# copy_odd_lines('file1.txt', 'file2.txt')