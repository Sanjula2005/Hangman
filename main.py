
import random
import hangman_art
import words

print(hangman_art.logo)

#randomly choose a word from the list, word_list.

chosen_word=random.choice(words.word_list)
#creating an empty list and appending a "_" for each letter in the chosen word.
display=[]
for i in range(len(chosen_word)):
  display.append("_")
print(display)

lives=6
 #repeating user input and replacement in display list.use while until it is not _  character 
you_loose=False
while not you_loose:
#ask the user for a letter input
  guess=input("Guess a letter: ").lower()
  clear()
  #to check if the chosen word is there in the chosen word 
  #replace the _ with the letter if it matches
  if guess in display:
    print(f"You have already guessed {guess}")
    
  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==guess:
      display[position]=letter

  if guess not in chosen_word:
    lives-=1
    print(f"you have guessed it wrong, you are left with {lives} lives")
    if lives==0:
      you_loose=True
      print("You loose")
    print(f"{' '.join(display)}")
  
  if "_" not in display:
    you_loose=True
  
  print(hangman_art.stages[lives])


print("The chosen word was",chosen_word)