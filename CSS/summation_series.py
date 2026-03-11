n = int(input("Enter number of terms: "))
total_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total_sum -= i
    else:
        total_sum += i
print(f"Summation of series: {total_sum}")