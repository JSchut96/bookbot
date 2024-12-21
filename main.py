path_to_file = "books/frankenstein.txt"

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}

    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    return char_count

def sort_on(dict):
    return dict["num"]

with open(path_to_file) as f:
    file_contents = f.read()
    print("--- Begin report of " + path_to_file + " ---")
    print(str(count_words(file_contents)) + " words were found in the document")
    print("")

    char_dict = count_characters(file_contents)
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

    for k, v in sorted_char_dict.items():
        print(f"The '{k}' character was found {v} times")
    

