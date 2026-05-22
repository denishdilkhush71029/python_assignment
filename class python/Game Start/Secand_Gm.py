import random

def shuffle(arr):
    # Fisher-Yates shuffle algorithm to randomly shuffle the points
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

def main():
    # Get player names from user input
    print("Enter the four players' names:")
    a = input("Player 1: ").strip()
    b = input("Player 2: ").strip()
    c = input("Player 3: ").strip()
    d = input("Player 4: ").strip()
    
    players = [a, b, c, d]
    points = [1000, 800, 500, 0]  # Points assigned randomly: thief = 0, accuser = 500
    
    while True:
        shuffle(points)
        
        # Show points only for players with 1000 or 500
        for i, p in enumerate(players):
            if points[i] == 1000 or points[i] == 500:
                print(f"{p}: {points[i]}")
        
        # Identify who has 500 (accuser) and who has 0 (thief)
        accuser_index = points.index(500) if 500 in points else -1
        thief_index = points.index(0) if 0 in points else -1
        
        if accuser_index != -1:
            accuser = players[accuser_index]
            guess = input(f"{accuser}, who is the thief? ").strip()
            actual_thief = players[thief_index]
            
            # Check if the guess is correct
            if guess == actual_thief:
                print("You are right!")
            else:
                print("You are wrong!")
                points[accuser_index] = 0
                # Assign 500 to someone else who is not the thief
                for i in range(4):
                    if points[i] == 0 and i != thief_index:
                        points[i] = 500
                        break
        
        # Ask to play again
        choice = input("Play again? (y/n): ").strip().lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()Copied!   