import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list= ["cameroon", "baboon", "elephant", "cow", "dog", "White" ]

chosen_word=random.choice(word_list)

lives=6

print(chosen_word)




display=[]  
for letter in chosen_word:
    display+="_"


end_of_game=False     
while not end_of_game :
   
  guess= input("Guess a random letter:\n").lower()  
  if guess in display:
    print("You have already guessed this letter")
 
  if guess not in chosen_word:
    lives-=1
    print("You have guessed a letter that is not in the word" ) 
    print(stages[lives])
  
  for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
          display[position]=letter
        


  print (f"{''.join(display)}")

  if "_" not in display:
    end_of_game=True
    print("You win") 
  if lives == 0:
    end_of_game=True
    
    print("You Lose!")