import random
from hangman_words import word_list
from hangman_art import stages,logo


chosen_word=random.choice(word_list)
lives=6
print("guess the word is",chosen_word)


print(logo)
print(len(stages))
display=[]
guessed=[]

for i in range(len(chosen_word)):
    display.append("_")

while "_" in display:
    guess=input("guess the letter:").lower()
    if len(guess)==1 and guess.isalpha():
        if guess in guessed:
            print('letter alrady is present')
            continue
        guessed.append(guess)
        for i in range(len(chosen_word)):
            letter=chosen_word[i]

            if letter==guess:
                display[i]=guess
        if guess not in chosen_word:
            lives=lives-1
            if lives==0:
                print('you lost!!!')
                print(stags[lives])
                print("the answer is",chosen_word)
                exit(1)

        print(f"{''.join(display)}")
        print(stages[lives])

else:print("great!!you have won")
