from stats import get_num_words, get_book_text, get_characters, sort_char_dict
import sys
# Use sys module to get command line arguments
def main(): 
  if len(sys.argv) != 2:
    sys.exit("Usage: python3 main.py <path_to_book>")
  pathfile = sys.argv[1]
  book_text = get_book_text(pathfile)
  num_words = get_num_words(book_text)
  char_count = get_characters(book_text)
  char_list = sort_char_dict(char_count)

  # print(char_count)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {pathfile}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("----------- Character Count ----------")
  for dictionary in char_list:
    character = dictionary["character"]
    count = dictionary["count"]
    if character.isalpha():
      print(f"{character}: {count}")
  print("============= END ===============")
    
main()
