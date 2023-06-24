import re

  ## print welcome message explaining process
print( """
  Welcome to MadLibs! Make up your own words to fill the prompts correctly to create a fun story. """)


  ## open and read template, turn into a string
def read_template(file_path):
  with open(file_path, 'r') as file:
    template = file.read()  ## template is a string 
    return template

def parse_template(template):
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
  return story_dict, tuple(whole_word_list)
      
  # print(story_list)
  # print(whole_word_list)

  ## Prompt user to submit words for required components  
  ## Take user input and populate template with the answers

def the_new_list(whole_word_list):
    new_whole_word_list = []
  
    for i in whole_word_list:
      user_input = input(f"Enter any word that is a(n) {i}")
      new_whole_word_list.append(user_input)
    print(new_whole_word_list)
    return tuple(new_whole_word_list)

  ## Write completed text to a new file 

  # for word in new_list:

def merge(story_dict, new_whole_word_tuple):
  new_whole_word_list = list(new_whole_word_tuple)
  pattern = r"\{([^}]*)\}"
  result = re.sub(pattern, lambda word: new_whole_word_list.pop(0), story_dict) # lambda is a mini function, iterating through new word list each time, then popping the 0 at index
    ## Provide the completed response back to user in command line
  print(result)
  return result

def write_to_file(file_path, mad_lib):
  with open(file_path, 'w') as file:
    file.write(mad_lib)



  ## Add at least one more "meaningful" test (not input/output) to the test file

if __name__ == '__main__':
  template = read_template('madlib.txt')
  stripped_template, parts = parse_template(template)
  the_new_list = the_new_list(parts)
  final_story = merge(stripped_template, the_new_list)
  write_to_file('finished_madlib.txt', final_story)
  parse_template(template)
