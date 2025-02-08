import random
#Makes the range for guessing
highest = int(input("\nHur högt vill du gissa?"))
answer = random.randint(1, highest)
#I want to make it so that a higher range for guessing gives more lives and higher score.
score = 0
guesses = 5

#to keep the loop going
is_true = True
final_score = 0
final_guesses = 0
print(f"Bra! Nu får du gissa på ett nummer mellan 1 och {highest}")

#while is_true == True: keeps my loop going

while is_true == True:
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
        
print(f"Du fick totalt {score} poäng och gjorde {final_guesses} gissningar totalt")
