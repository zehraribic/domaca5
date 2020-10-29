import json
import random
import datetime

curent_time = datetime.datetime.now()
secret = random.randint(1, 30)
player_name = input("Input your name: ")
level = input("Would you like E) easy level or H) hard level? Input E or H: ")
level = level.lower()
attempts = 0
wrong_attempts = 0

# Definiranje funkcije za težavnost igre
def play_game(level):
    if level == "h":
        return ("Your guess is not correct... try again")
    elif level == "e" and guess > secret:
        return ("Your guess is not correct... try something smaller")
    else:
        return ("your guess is not correct...try something bigger")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]  # Sortirani rezultati

    # Zapis vseh rezultatov
    for score_dict in score_list:
        print("Top score: " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"),
              ", player name: " + score_dict["player name"])

# Branje in zapis napačnih poskusov
with open("wrong_guesses.txt", "r") as wrongguesses_file:
    wrong_guesses = json.loads(wrongguesses_file.read())
    print(str(wrong_attempts))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "player name": player_name, "date": str(datetime.datetime.now())})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("you've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")
        selection = selection.lower()  # Pretvorba v male črke

        if selection == "a":
            secret = random.randint(1, 30)
            attempts = 0
            wrong_attempts = 0

        elif selection == "b":
            score_list = sorted(score_list, key=lambda k: k["attempts"])[:1]  #Izpis najboljšega rezultata
            for score_dict in score_list:
                print("Best score: " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"),
                  ", player name: " + score_dict["player name"])
            break
        else:
             break

    elif guess > secret:
        wrong_attempts += 1
        wrong_guesses.append({"wrong attempts": wrong_attempts})

        with open("wrong_guesses.txt", "w") as wrongguesses_file:
            wrongguesses_file.write(json.dumps(wrong_guesses))

        print(play_game(level))   #klic funkcije za težavnost igre
        print("Number of wrong attempts: " + str(wrong_attempts))

    elif guess < secret:
        wrong_attempts += 1
        wrong_guesses.append({"wrong attempts": wrong_attempts})

        with open("wrong_guesses.txt", "w") as wrongguesses_file:
            wrongguesses_file.write(json.dumps(wrong_guesses))

        print(play_game(level)) #klic funkcije za težavnost igre
        print("Number of wrong attempts: " + str(wrong_attempts))