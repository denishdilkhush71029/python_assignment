try:
    nums = input("Enter numbers (space separated): ").split()
    if len(nums) != len(set(nums)):
        raise Exception("Duplicate numbers detected!")
    print("No duplicates found.")
except Exception as e:
    print(e)