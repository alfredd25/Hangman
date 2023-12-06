import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=['apple','orange','banana','cherry','papaya',
'pomegrenate','kiwi','litchi','strawberry','watermelon','dragonfruit','muskmelon']
chosen_word=random.choice(word_list)
display=[]
lives=6
length=len(chosen_word)
for i in range(0,length):
        display.append('_')
print(display)
while True:
    
    user_letter=input("Guess a letter:").lower()
    if user_letter in display:
        print(f"You have already entered {user_letter}")
    for letter in range(0,length):
        if user_letter==chosen_word[letter]:
            display[letter]=user_letter
    print(display)
    
    if user_letter not in chosen_word:
        print(f"No match {user_letter} is not in the word. You lose a life")
        lives-=1
    print(stages[lives])
    if lives==0:
        print(f"The word was {chosen_word}")
        print("You ran out of lives")
        print("YOU LOSEEEEEE")
        break
            
    
    if '_' not in display:
        print("You have WON")
        break
