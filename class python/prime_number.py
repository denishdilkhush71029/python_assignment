num=int(input("Enter the number of n:"))
if num > 1:
    is_prime = True
    for i in range(2,num):
        if (num % i) == 0:
            is_pime = false
            break
        if is_prime:
            print(f"{num} is a prime number")
            else:
                print(f"{num} id not a prime number")
            else:
                print(f"{num} is not a prime number")