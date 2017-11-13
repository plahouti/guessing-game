import random
import time

p1guesses = 0
p2guesses = 0
p1rounds = 0
p2rounds = 0

def hard2():
    print("You have chosen to play the hard level!")
    time.sleep(2)
    hard()

def medium2():
    print("You have chosen the medium level!")
    time.sleep(2)
    medium()

def easy2():
    print("You have chosen the easy level!")
    time.sleep(2)
    easy()

def easy():
    global p1guesses, p2guesses, p1rounds, p2rounds
    num = random.randrange(1, 25)
    print(p1 + ", it is your turn")
    time.sleep(2)
    print("Remember, whoever uses up 10 guesses first loses a round. First to lose 3 rounds loses.")
    time.sleep(2)
    while True:
        guess1 = input("Guess a number between 1 and 25.")
        if guess1 < num:
            print("The number you entered is too low. Please guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 10:
                print("Sorry, you lost because you made 10 incorrect guesses.")
                p1guesses = 0
                p2guesses = 0
                time.sleep(2)
                p2rounds = p2rounds + 1
                if p2rounds == 3:
                    print("Congratulations, " + p2 + ". You have won!")
                    break
                easy()
                break
        elif guess1 > num:
            print("The number you guessed is too high. Please guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 10:
                print("Sorry, you lost because you made 10 incorrect guesses.")
                p1guesses = 0
                p2guesses = 0
                time.sleep(2)
                p2rounds = p2rounds + 1
                if p2rounds == 3:
                    print("Congratulations, " + p2 + ". You have won!")
                    break
                easy()
                break
        elif guess1 == num:
            print("Congratulations, " + p1 + " you correctly guessed the number!")
            time.sleep(3)
            print("You now have " + str(p1guesses) + " guesses.")
            time.sleep(3)
            print(p2 + ", it is your turn")
            time.sleep(2)
            print("Remember, whoever reaches 10 guesses first loses.")
            time.sleep(2)
            num = random.randrange(1, 25)
            while True:
                guess2 = input("Guess a number between 1 and 10")
                if guess2 < num:
                    print("The number you entered is too low. Please guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 10:
                        print("Sorry, you lost because you made 10 incorrect guesses.")
                        p1guesses = 0
                        p2guesses = 0
                        time.sleep(2)
                        p1rounds = p1rounds + 1
                        if p1rounds == 3:
                            print("Congratulations, " + p2 + ". You have won!")
                            break
                        easy()
                        break
                elif guess2 > num:
                    print("The number you guessed is too high. Please guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 10:
                        print("Sorry, you lost because you made 10 incorrect guesses.")
                        p1guesses = 0
                        p2guesses = 0
                        time.sleep(2)
                        p1rounds = p1rounds + 1
                        if p1rounds == 3:
                            print("Congratulations, " + p2 + ". You have won!")
                            break
                        easy()
                        break
                elif guess2 == num:
                    print("Congratulations, " + p2 + " you correctly guessed the number!")
                    time.sleep(3)
                    print(p1 + " total guesses: " + str(p1guesses))
                    print(p2 + " total guesses: " + str(p2guesses))
                    time.sleep(2)
                    print("Let's keep going")
                    easy()




def medium():
    global p1guesses, p2guesses, p1rounds, p2rounds
    num = random.randrange(1, 50)
    print(p1 + ", it is your turn")
    time.sleep(2)
    print("Remember, whoever uses up 15 guesses first loses a round. First to lose 3 rounds loses.")
    time.sleep(2)
    while True:
        guess1 = input("Guess a number between 1 and 50.")
        if guess1 < num:
            print("The number you entered is too low. Please guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 15:
                print("Sorry, you lost because you made 15 incorrect guesses.")
                p1guesses = 0
                p2guesses = 0
                time.sleep(2)
                p2rounds = p2rounds + 1
                if p2rounds == 3:
                    print("Congratulations, " + p2 + ". You have won!")
                    break
                medium()
                break
        elif guess1 > num:
            print("The number you guessed is too high. Please guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 15:
                print("Sorry, you lost because you made 15 incorrect guesses.")
                p1guesses = 0
                p2guesses = 0
                time.sleep(2)
                p2rounds = p2rounds + 1
                if p2rounds == 3:
                    print("Congratulations, " + p2 + ". You have won!")
                    break
                medium()
                break
        elif guess1 == num:
            print("Congratulations, " + p1 + " you correctly guessed the number!")
            time.sleep(3)
            print("You now have " + str(p1guesses) + " guesses.")
            time.sleep(3)
            print(p2 + ", it is your turn")
            time.sleep(2)
            print("Remember, whoever reaches 15 guesses first loses.")
            time.sleep(2)
            num = random.randrange(1, 50)
            while True:
                guess2 = input("Guess a number between 1 and 50")
                if guess2 < num:
                    print("The number you entered is too low. Please guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 15:
                        print("Sorry, you lost because you made 15 incorrect guesses.")
                        p1guesses = 0
                        p2guesses = 0
                        time.sleep(2)
                        p1rounds = p1rounds + 1
                        if p1rounds == 3:
                            print("Congratulations, " + p2 + ". You have won!")
                            break
                        medium()
                        break
                elif guess2 > num:
                    print("The number you guessed is too high. Please guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 15:
                        print("Sorry, you lost because you made 15 incorrect guesses.")
                        p1guesses = 0
                        p2guesses = 0
                        time.sleep(2)
                        p1rounds = p1rounds + 1
                        if p1rounds == 3:
                            print("Congratulations, " + p2 + ". You have won!")
                            break
                        medium()
                        break
                elif guess2 == num:
                    print("Congratulations, " + p2 + " you correctly guessed the number!")
                    time.sleep(3)
                    print(p1 + " total guesses: " + str(p1guesses))
                    print(p2 + " total guesses: " + str(p2guesses))
                    time.sleep(2)
                    print("Let's keep going")
                    medium()

def hard():
    global p1guesses, p2guesses, p1rounds, p2rounds
    num = random.randrange(1, 1000)
    print(p1 + ", it is your turn")
    time.sleep(2)
    print("Remember, whoever uses up 30 guesses first loses a round. First to lose 3 rounds loses.")
    time.sleep(2)
    while True:
        guess1 = input("Guess a number between 1 and 1000.")
        if guess1 < num:
            print("The number you entered is too low. Please guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 30:
                print("Sorry, you lost because you made 30 incorrect guesses.")
                p1guesses = 0
                p2guesses = 0
                time.sleep(2)
                p2rounds = p2rounds + 1
                if p2rounds == 3:
                    print("Congratulations, " + p2 + ". You have won!")
                    break
                hard()
                break
        elif guess1 > num:
            print("The number you guessed is too high. Please guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 30:
                print("Sorry, you lost because you made 30 incorrect guesses.")
                p1guesses = 0
                p2guesses = 0
                time.sleep(2)
                p2rounds = p2rounds + 1
                if p2rounds == 3:
                    print("Congratulations, " + p2 + ". You have won!")
                    break
                hard()
                break
        elif guess1 == num:
            print("Congratulations, " + p1 + " you correctly guessed the number!")
            time.sleep(3)
            print("You now have " + str(p1guesses) + " guesses.")
            time.sleep(3)
            print(p2 + ", it is your turn")
            time.sleep(2)
            print("Remember, whoever reaches 30 guesses first loses.")
            time.sleep(2)
            num = random.randrange(1, 1000)
            while True:
                guess2 = input("Guess a number between 1 and 1000")
                if guess2 < num:
                    print("The number you entered is too low. Please guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 30:
                        print("Sorry, you lost because you made 30 incorrect guesses.")
                        p1guesses = 0
                        p2guesses = 0
                        time.sleep(2)
                        p1rounds = p1rounds + 1
                        if p1rounds == 3:
                            print("Congratulations, " + p2 + ". You have won!")
                            break
                        hard()
                        break
                elif guess2 > num:
                    print("The number you guessed is too high. Please guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 30:
                        print("Sorry, you lost because you made 30 incorrect guesses.")
                        p1guesses = 0
                        p2guesses = 0
                        time.sleep(2)
                        p1rounds = p1rounds + 1
                        if p1rounds == 3:
                            print("Congratulations, " + p2 + ". You have won!")
                            break
                        hard()
                        break
                elif guess2 == num:
                    print("Congratulations, " + p2 + " you correctly guessed the number!")
                    time.sleep(3)
                    print(p1 + " total guesses: " + str(p1guesses))
                    print(p2 + " total guesses: " + str(p2guesses))
                    time.sleep(2)
                    print("Let's keep going")
                    hard()


def level():
    print("There are 3 difficulties to this game. They are easy(1-25), medium(1-50), and hard(1-1000).")
    time.sleep(1.5)
    difficulty = raw_input("Which level of difficulty would you like to play?")
    if difficulty == "1" or difficulty == "easy" or difficulty == "Easy":
        easy2()
    elif difficulty == "2" or difficulty == "medium" or difficulty == "Medium":
        medium2()
    elif difficulty == "3" or difficulty == "hard"or difficulty == "Hard":
        hard2()




def main():
    global p1
    global p2
    print("Welcome to the world renowned Guessing Game!")
    time.sleep(3)
    p1 = raw_input("Player 1: What is your name?")
    print("Welcome, " + p1 + ". The objective of this game is to guess the randomly generated number.")
    p2 = raw_input("Player 2: What is your name?")
    print("Welcome, " + p2 + ". The objective of this game is to guess the randomly generated number.")
    print("The program will tell you to either guess lower or higher if you are off.")
    time.sleep(4)
    print("The first to lose 3 rounds loses.")
    time.sleep(1.5)
    level()

main()