import random
from hollywood_actors import word_list
from hangman_art import stages, logo

# for while loop
endgame = False
chosen_word = random.choice(word_list)

# creating variable to keep track of stages
lives = 6
print(logo)

# create list which will display how much blank spaces ["_"] are remaining as well as how much is filled,
# for eg: if chosen_word = "apple" and if you guess letter p then display = ["_","p","p","_","_"]
display = []
for letter in chosen_word:
    display += "_"


while not endgame:
    # input for user to enter
    guess = input("guess a letter:").lower()

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(display)
    else:
        print(stages[lives])
        lives = lives - 1
        print("lives remaining:", lives)

    if "_" not in display:
        endgame = True
        print("Congratulations!! You Win")

    if lives == 0:
        endgame = True
        print("Oh! You Loose")
