#Exercise 1
#Objective**: given the list of words below, create a function that checks if the word is a palindrome or not and then separates the palindrome words from  the ones are not.

#What is a palindrome?
#A word is said to be palindrome if the reverse of the word is the same as original word.

#What your function must return: a dictionary with two entries. 
#One entry should contain a list of the palindrome words and the other entry should contain a list of words that are not palindromes.

#Baby steps:
#1.  First concentrate in writing the code that identifies a palindrome word
#2.  Then, create two lists: one where you'll put the palindrome words and  another one where you'll put the words that are not palindromes. 
#3.  Last step is the easy one, you only have to add the lists to a dictionary.

#Tips: remember to lower case the words. You can reverse a string in a'pythonic' way using list slices as in [::-1]
--------------------------------------------------------------------------------------

words = ['Abba', 'Arara', 'Banana', 'aaaa',
         'Zebra', 'Madam', 'Mouse', 'Civic',
         'Dad', 'Mom', 'Giant', 'accca', 'Radar',
         'Virus', 'Gig', 'Zombie', 'Garlic']

# We will use two funcions

def is_palindrome(word):
  #This function only checks if a word is a palindrome and returns yes or no
  word = word.lower() #We lowercase the word
  if word == word[::-1]: #We check if the word is the same as its backward spelling (if it's an actual palindrome)
    return 'yes'
  else:
    return 'no'

def get_palindromes(words): 
  #Here we create a dictionary with two keys and for values, we create emtpy lists
  pal_dict = {'palindrome': [], 'non-palindrome':[]}
  for word in words: #We iterate through each word and check if they are a palindrome or not and we add them to the dictionary
    if is_palindrome(word) == 'yes':
      pal_dict['palindrome'].append(word)
    else:
      pal_dict['non-palindrome'].append(word)
  return pal_dict # We return the dictionary

get_palindromes(words)

#Exercise 2
#Objective: Given the list of strings of the first exercise, write a function that counts the number of words where the string length
#is 2 or more and the first and last character are the same.

#Tips: use the indexes to get the first and last character of a word. Remember that the index -1 corresponds to the last element.

def process(words):
  longer_2_same_first_end_char = 0 #We create a variable count that starts at 0
  for word in words:
    word = word.lower() #We lowercase the word
    # We use two condtions:
    # 1. If the word length is bigger than two
    # 2. If the word's first char (word[0]) is the same as the last one (word[-1])
    if len(word) >= 2 and word[0] == word[-1]: 
      longer_2_same_first_end_char += 1
  return longer_2_same_first_end_char

process(words)

#Exercise 3
#Given the list of strings of the first exercise, write a function that returns the rounded average word length.

def get_average_len(words):
  all_lens = [] #We create an empty list
  for word in words:
    all_lens.append(len(word)) #We add the lengths of each word
  avg_len = round(sum(all_lens)/len(words),0) #we sum all lengths, we divide them by the number of words and finally, we round the number so it is not a float
  return avg_len

get_average_len(words)
