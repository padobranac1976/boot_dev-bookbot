import sys
from stats import count_words, char_stats, convert_dict

def get_book_text(file_path):
    with open(file_path) as f:    
        file_contents = f.read()    
    return file_contents

def print_report(words, dict_list, path):
    print(12*"=" + " BOOKBOT " + 12*"=")
    print(f"Analyzing book found at {path}...")
    print(11*"-" + " Word Count " + 10*"-")
    print(f"Found {words} total words")
    print(9*"-" + " Character Count " + 7*"-")
    for d in dict_list:
        print(f'{d["char"]}: {d["num"]}')
    print(13*"=" + " END " + 15*"=")


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    relative_path = args[1]
    output = get_book_text(relative_path)
    words = count_words(output)
    char_hist = char_stats(output)
    dict_list = convert_dict(char_hist)
    print_report(words, dict_list, relative_path)
    
    

if __name__ == "__main__":
    main()
