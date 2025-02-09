import random
#Makes the range for guessing
def get_highest():
    while True:
        try:
            highest = int(input("\nHur högt vill du gissa?"))
            return highest
        except ValueError:
            print("Skriv ett nummer")
            continue
        
def game(highest):
    global final_score, final_guesses
    answer = random.randint(1, highest)
    score = 0
    guesses = 5
    final_score = 0
    final_guesses = 0
    print(f"Bra! Nu får du gissa på ett nummer mellan 1 och {highest}")
    while True:
        guess = int(input("Skriv din gissning här: "))
        print(str(answer))
        if guess == answer:
            print("Rätt! Du får ett poäng")
            score += 1
            final_score += 1
            final_guesses += 1
            print(f"Dina poäng: {score}")
            answer = random.randint(1, highest) # generates a new number when guessing right
        elif guess != answer:
            print("Fel! Du förlorade ett liv.")
            guesses -= 1
            final_guesses += 1
            print(f"Liv kvar: {guesses}")
        if score == 5:
            print("Du vann spelet!")
            again = input("Vill du spela igen? Y/N:")
            if again.lower() == "y":
                score = 0
            elif again.lower() == "n": 
                print("Kul att du spelade!")
                break
            else:
                print("error")
                break
        elif guesses == 0:
            print("Du förlorade!")
            again = input("Vill du ha revansch? Y/N:")
            if again.lower() == "y":
                guesses = 5
            elif again.lower() == "n": 
                print("Kul att du spelade!")
                break
            else:
                print("error")
                break

def play_again():
    again = input("Vill du spela igen? Y/N:")
    if again.lower() == "y":
        score = 0
    elif again.lower() == "n": 
        print("Kul att du spelade!")
    else:
        print("error")
    return score
highest = get_highest()
game(highest)
print(f"Du fick totalt {final_score} poäng och gjorde {final_guesses} gissningar totalt")

