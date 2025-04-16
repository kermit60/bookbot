# a file that contains functions for analyzing the text
def get_book_text(filepath):
  # The with block can be used to open a file, it automatically closes the file when the block is exited
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
# gets the number of words in a string
def get_num_words(book_text):
  book_list = book_text.split()
  return len(book_list)
# gets the number of characters and its count
def get_characters(book_text):
  character_dict = {}
  for char in book_text:
    char = char.lower()
    character_dict[char] = 1 + character_dict.get(char, 0)
  return character_dict

def sort_on(dict):
  return dict["count"]
# returns a list of character and its count
def sort_char_dict(char_dict):
  char_list = []
  for key in char_dict:
    char_list.append({
      "character": key,
      "count": char_dict[key]
    })
  char_list.sort(reverse=True, key=sort_on)
  return char_list
