import random
import jk


lives=6
random_word=random.choice(jk.WORDS)
print(random_word)
placeholder=""
for position in range(len(random_word)):
    placeholder+="_"
print(placeholder)
lives=6




game_over=False
correctletters=[]
while not game_over:
    guess=input("Guess a letter:").lower()
    display=""
    for letter in random_word:
        if letter==guess:
            display+=letter
            correctletters.append(letter)
        elif letter in correctletters:
            display+=letter

        else:
            display+="_"
    print(display)
    if guess not in random_word:
        lives=lives-1
        if lives==0:
            print("you lose")
    print("lives",lives)


    if "_" not in display:
        game_over=True
        print("you win")
