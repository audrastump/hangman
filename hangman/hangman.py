
import arcade
import hangmanArt
from random_word import RandomWords
runs = ['''
  #---#
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  #---#
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  #---#
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  #---#
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  #---#
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  #---#
  |   |
  O   |
      |
      |
      |
=========
''', '''
  #---#
  |   |
      |
      |
      |
      |
=========
The noose tightens around your neck... you have the sudden urge to urinate
''']

logo = ''' 
 _   _                                          
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __| |                      
                   |___/    '''

print(logo)

r = RandomWords()

secretword = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=10, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=3, minLength=5, maxLength=10)
lettersGuessed = ""
failureCount = 0

while failureCount<6:
    guess = input("Please enter your letter \n")
    
    
    if guess in lettersGuessed:
        print(f"You already guessed {guess}, please try another letter")
    elif guess in secretword:
        print(f"Correct, there is one or more {guess} in the secret word")
    else:
        failureCount+=1
        print(f"Incorrect, there no {guess} in the secret word")
    lettersGuessed = lettersGuessed+guess
    incorrectLetters = 0
    for letter in secretword:
        if letter in lettersGuessed:
            print(f"{letter}",end="")
        else:
            print(f"_",end="") 
            incorrectLetters+=1
    print("\n")
    if incorrectLetters==0:
        print(f"You guessed the secret word")
        break
    print(runs[failureCount])
if incorrectLetters != 0:
    print("You ran out of guesses! The word was "+secretword)