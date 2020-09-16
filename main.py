from random_word import RandomWords
from random_word import RandomWords
import re

class GameInterface:

   guess_word = ""
   current_word = ""
   used_letters = []
   def __init__(self, life):
       self.life = life
    # Generates random word
   def generate_word(self):
       r = RandomWords()
       self.guess_word = r.get_random_word()

    # The main fuction
   def start_game(self):
       self.generate_word()
       self.current_word = "_" * len(self.guess_word)
       while self.check_endgame_condition():
           letter = self.ask_for_letter()
           self.check_guess_word(letter)
           self.print_game_state()
       if self.life == 0:
           print(f"You lose! \n The word was {self.guess_word}")
       else:
           print("You won")

    # Checks if player is wins or lose
   def check_endgame_condition(self):
       return not(self.life == 0 or self.guess_word == self.current_word)
                    # Returns if life is 0 or the word is guessed

    # Takes the input letter and checks if input is valid
   def ask_for_letter(self):
       print ("Type letter: ")
       letter = input().lower()
       while re.finditer("[a-z]", letter) == None or len(letter) != 1:
           # Returns error if input is longer then 1 letter or it isnt a letter
           print("Invalid input")
           letter = input().lower()
       return letter

   # Checks if input letter matches the letter in word
   def check_guess_word(self, letter):
       match = list(re.finditer(letter, self.guess_word))
       # Checks how many letters has been matched

       if len(match) == 0:
           self.life -= 1
           self.used_letters.append(letter)
       # If input letter has no matches, player loses life.

       else:
           substrings = []
           init_index = 0
           for i in match:
               index = i.regs[0][0]
               substrings.append(self.current_word[init_index:index])
               init_index = index + 1
           substrings.append(self.current_word[init_index::])
           self.current_word = letter.join(substrings)
    # Chaanges every "_" to input letter it found

   def print_game_state(self):
       print(f"Remaining lifes: {self.life} \n Current word: {self.current_word}\n used letters:{self.used_letters} ")

if __name__ == "__main__":
   game = GameInterface(10)
   game.start_game()

