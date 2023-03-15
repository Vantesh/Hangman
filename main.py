import random

from ASCII_art import stages
from word_list import word_list

chosen_word=random.choice(word_list)

lives=6

display=[]  
for letter in chosen_word:
    display+="_"


end_of_game=False
     
while not end_of_game :
   
  guess= input("Guess a random letter: ").lower()  
  if guess in display:
    print("\nYou have already guessed this letter")
 
  if guess not in chosen_word:
    lives-=1
    print("\nYou have guessed a letter that is not in the word\n\n" ) 
    print(f"You have {lives} live(s) left:\n" , stages[lives])
  
  for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
          display[position]=letter
        


  print (f"{''.join(display)}")

  if "_" not in display:
    end_of_game=True
    print("\nYou win 😱🤩🎉") 
  if lives == 0:
    end_of_game=True
    
    print("\nYou Lose! ☠️")