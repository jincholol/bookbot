from stats import get_num_words, get_char_count, sort_report, sorted_dictionaries
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        book_content = f.read()
    return book_content


def main():
   
   if len(sys.argv) == 2: 
    book_text = get_book_text(sys.argv[1]) 
   else:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1) 
   num_words = get_num_words(book_text)
   char_count = get_char_count(book_text)
   print((f"Found {num_words} total words"))
   print((f"{char_count}"))
   report = sorted_dictionaries(char_count)
   for item in report:
       character = item["char"]
       count = item["num"]
       if character.isalpha():
        print(f"{character}: {count}")

                 
           
main()