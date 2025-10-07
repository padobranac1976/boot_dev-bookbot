from stats import count_words, char_stats

def get_book_text(file_path):
    with open(file_path) as f:    
        file_contents = f.read()    
    return file_contents


def main():
    relative_path = "books/frankenstein.txt"
    output = get_book_text(relative_path)
    words = count_words(output)
    print(f"Found {words} total words")
    
    char_hist = char_stats(output)
    print(char_hist)

if __name__ == "__main__":
    main()
