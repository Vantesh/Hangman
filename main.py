import random
word_list= ["cameroon", "baboon", "elephant", "cow", "dog", "White" ]

chosen_word=random.choice(word_list)


print(chosen_word)




display=[]  
for letter in chosen_word:
    display+="_"
end_of_game=False     
while not end_of_game :
   
  guess= input("Guess a random letter:\n").lower()  
  
       
  for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
          display[position]=letter


  print (display)

  if "_" not in display:
    end_of_game=True
    print("You win") 