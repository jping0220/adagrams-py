import random

LETTER_POOL = {
    "A":9, "B":2, "C":2, "D":4, "E":12, "F":2, "G":3, "H":2,
    "I":9, "J":1, "K":1, "L":4, "M":2, "N":6, "O":8, "P":2,
    "Q":1, "R":6, "S":4, "T":6, "U":4, "V":2, "W":2, "X":1,
    "Y":2, "Z":1
}

LETTER_VALUES = {
   "A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4,
    "I":1, "J":8, "K":5, "L":1, "M":3, "N":1, "O":1, "P":3,
    "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "X":8,
    "Y":4, "Z":10 
}

def draw_letters():
    letters = [] 
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency): 
            letters.append(letter) 
    selected_letters = []
    for i in range(10):
        letter = random.choice(letters)
        selected_letters.append(letter)
        letters.remove(letter) # remove letter to avoid over drawing 
    return selected_letters 
        

def uses_available_letters(word, letter_bank):
    letters = list(letter_bank) # made another cophy to avoid modify original letter bank  
    for letter in word.upper(): 
        if letter not in letters: 
            return False
        letters.remove(letter) 
    return True


def score_word(word):
    score = 0
    for letter in word.upper(): 
        score += LETTER_VALUES[letter] 
    if len(word) >= 7: 
        score += 8
    return score 


def get_highest_word_score(word_list):
    highest_score = 0
    highest_word_list = [] 
    for word in word_list:
        score = score_word(word) 
        if score > highest_score:
            highest_score = score
            highest_word_list = [word] 
        elif score == highest_score: 
            highest_word_list.append(word)

    min_word = highest_word_list[0] # set the first word & assume it's the shortest word 
    min_len = len(min_word) 
    for word in highest_word_list:
        if len(word) == 10: 
            return (word, highest_score)
        elif len(word) < min_len:
            min_len = len(word)   
            min_word = word           
    return (min_word, highest_score) 


