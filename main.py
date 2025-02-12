def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_num_characters(text)

    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for char_info in char_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")
        
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


def get_num_characters(text):
    char_count = {}
    lower_char = text.lower()
    for char in lower_char:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
main()