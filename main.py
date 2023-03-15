import random
word_list= ["Cameroon", "Baboon", "Elephant"]
word=random.choice(word_list)

guess= input("Guess a random letter:\n").lower()

for letter in word:
  if letter == guess:
    print("right")
  else:
    print("Wrong")