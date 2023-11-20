#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.


import random

word_range = random.randrange(0, 3)
chosen_word = word_list[word_range]


# chosen_word = random.choice(word_list)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Masukkan Huruf tebakan anda? ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

i = 0
while i < len(chosen_word):
  if guess in chosen_word[i]:
    print("True")
  else:
    print("False")
  i = i + 1

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")