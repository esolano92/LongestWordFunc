#promts user to input a string saves it to sentence variable
sentence = input("Type a sentence to find the longest word.\n")

#function that returns the longest word in a string
def find_longest_word(sentence):
  #split function splits the string by spaces and saves into a word list
  word = sentence.split(" ")
  longest_word = ""

  #iterate through each index of the word list if the word at the specified index is lager than "longest_word" save that "word" into variable "longest_word"
  for number in range(len(word)):
    if len(word[number]) > len(longest_word):
     longest_word = word[number]
  return longest_word

#prints the longest word for the user
print(f"The longest word in the sentecne you provided is {find_longest_word(sentence)}") 
