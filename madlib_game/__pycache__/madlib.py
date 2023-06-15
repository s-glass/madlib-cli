import re
from tests.test_madlib import *
whole_word_list = ["Adjective"]

def main():
  ## print welcome message explaining process
  print( """
  Welcome to MadLibs! Make up your own words to fill the prompts correctly to create a fun story. """)


  ## open and read template, turn into a string
  with open('madlib_template.txt', 'r') as file:
    template = file.read()  ## template is a string 

  non_curly = False
  story_dict = ''
  story_list = []
  empty_filler = ''
  whole_word_list = []
  ignore = ["{","}"]
  new_list = []  # list of all the new words

  ## parse template into usable parts
  for char in template:
      if char == "}":
        whole_word_list.append(empty_filler)
        empty_filler = ''
        non_curly = False

      if char == "{":
        non_curly = True   #when changing value, single =
        story_list.append(story_dict)
        story_dict = ''

      if non_curly == False:
        if char not in ignore:
          story_dict += char 

      else:
        if char not in ignore:
          empty_filler += char
      
  # print(story_list)
  # print(whole_word_list)

  ## Prompt user to submit words for required components  
  ## Take user input and populate template with the answers
  for i in whole_word_list:
    user_input = input(f"Enter any word that is a(n) {i}")
    temp = new_list.append(user_input)

  print(new_list)


  ## Write completed text to a new file 

  # for word in new_list:
  pattern = r"\{([^}]*)\}"
  result = re.sub(pattern, lambda word: new_list.pop(0), template) # lambda is a mini function, iterating through new word list each time, then popping the 0 at index
  # print(result)


  with open('finished_madlib.txt', 'w') as file:
    template = file.write(result)

  ## Provide the completed response back to user in command line
  print(result)

  ## Add at least one more "meaningful" test (not input/output) to the test file

if __name__ == '__main__':
  main()

