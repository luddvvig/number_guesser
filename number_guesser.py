import random

def read_highscore(filename="highscore.txt"):
    try:
        with open("highscore.txt", "r") as f:
            highscore = [int(line.strip()) for line in f]
            highscore.sort(reverse=True)
            return highscore
    except FileNotFoundError:
        return []  # Return empty list if file not found
    except ValueError: #Handle if there is a non-int in the file
        print("Invalid highscore file format. Starting with empty highscores.")
        return []

def append_highscore(score, filename="highscore.txt", max_scores=5):
    highscore = read_highscore(filename)

    highscore.append(score)
    highscore.sort(reverse=True)
    highscore = highscore[:max_scores]

    with open("highscore.txt", "w") as f:
        for score in highscore:
            f.write((str(score)) + "\n")



def starter_input():
    global playing_range, name
    name = input("Enter player name: ")
    print(f"Welcome {name}!")
    playing_range = int(input("Enter the range you want to play in: "))
    return playing_range, name

def over_under(answer, guess):
    if guess < answer:
        print("The answer is higher")
    elif guess > answer:
        print("The answer is lower")
    else:
        print("TError")

def game(playing_range, name):
    answer = int(random.randrange(1, playing_range))
    global final_guesses, final_score, score
    score = 0
    guesses = 5 
    final_score = 0
    final_guesses = 0
    print(f"Great {name} Now you can guess a number between 1 and {playing_range}")

    
    while True:
        guess = int(input("Enter your guess here: "))
        print(guesses)
        if guess == answer:
            print("Correct! You get a point")
            score += 1
            final_score += 1
            final_guesses += 1
            print(f"{name}s score: {score}")
            answer = random.randint(1, playing_range)
        elif guess != answer:
            print("Wrong! You lost a life.")
            over_under(answer, guess)
            guesses -= 1
            final_guesses += 1
            print(f"{name}s guesses left: {guesses}")
        if score == 5:
            print("You won the game!")
            if play_again() == True:
                score = 0
            else:
                break
        elif guesses == 0:
            print("You lost!")
            if play_again() == True:
                guesses = 5
            else:
                break
    return score
            
def play_again():
    while True:
        again = input("Do you want to play again? Y/N: ").lower()
        if again == "y":
            return True
        elif again == "n":
            print("Kul att du spelade!")
            print(f"Du fick totalt {final_score} poäng och gjorde {final_guesses} gissningar totalt")

            return False
        else:
            print("Ogiltigt val, vänligen ange Y eller N.")

def main():
    starter_input()
    game(playing_range, name)
    append_highscore(final_score)
    highscores = read_highscore()
    print("\nHigh Scores:")
    for i, score in enumerate(highscores):
        print(f"{i+1}. {score}")

if __name__ == "__main__":
    main()