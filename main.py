def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = word_counter(text)
    letter_count = letter_counter(text)
    letter_list = sort_letters(letter_count)
    def letter_sentences(list):
        sentences = ""
        for item in list:
            sentences += f"The '{item["letter"]}' character was found {item["count"]} times.\n"
        return sentences.strip()
    print(f"--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document.\n")
    print(letter_sentences(letter_list))
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_counter(text):
    words = text.split()
    return len(words)

def letter_counter(text):
    lower_text = text.lower().replace(" ","")
    letters_dict = {}
    for letter in lower_text:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return letters_dict

def sort_on(dict):
    return dict["letter"]

def sort_letters(dict):
    letters_list = []
    for entry, count in dict.items():
        if entry.isalpha() == True:
            letters_list.append({"letter": entry, "count": count})
        else:
            pass
    letters_list.sort(key=sort_on, reverse=False)
    return letters_list


main()