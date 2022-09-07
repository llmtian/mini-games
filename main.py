import random

# Mini Game 1: Rock, Paper, Scissors

def mini_game_1() -> None:
    a = input("Enter 'Rock', 'Paper', or 'Scissors': ")
    b = input("Enter 'Rock', 'Paper', or 'Scissors': ")
    valid_input = ["Rock", "Paper", "Scissors"]
    if a not in valid_input or b not in valid_input:
        print("Error")
        return

    if a == b:
        print("Tie")
    else:
        if a == "Rock" and b == "Paper":
            print("Paper wins")
        elif a == "Paper" and b == "Scissors":
            print("Scissors Wins")
        elif a == "Scissors" and b == "Rock":
            print("Rock Wins")


# Mini Game 2: Guess the number

def mini_game_2() -> None:
    min = 1
    max = 9
    n = random.randint(min, max)
    c = 0

# For checking:
# print(f"{n} is the correct answer.")

    s = input("Guess the number between 1 and 9 or type exit to end the game: ")
    if s == "exit":
        print("End game.")
        print(f"You have guessed {c} times.")
        return

    a = int(s)
    c += 1

    while a != n:
        if a > n:
            print("Lower")
        elif a < n:
            print("Higher")

        s = input("Incorrect! Try again or type exit to end the game: ")
        if s == "exit":
            print("End game.")
            print(f"You have guessed {c} times.")
            return
        else:
            a = int(s)
            c += 1

    print("Your are right!")
    print(f"You have guessed {c} times.")


if __name__ == '__main__':

# remove the "#" to try out the games

    # mini_game_1()

    # mini_game_2()

