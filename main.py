def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")

    content_book = get_book(book_path)
    total_words = count_words(content_book)
    print(f"{total_words} words found in the document")

    total_characters = count_chars(content_book)
    list_total_chars = converto_to_list_of_dict(total_characters)
    list_total_chars.sort(reverse=True, key=sort_on)

    for i in list_total_chars:
        print(f"The '{i["char"]}' character was found {i["num"]} times")

    print("--- End report ---")


def get_book(path):
    with open(path) as f:
        return f.read()


def count_words(text=""):
    splited_book_text = text.split()
    return len(splited_book_text)


def count_chars(text=""):
    characters = {}
    text_lowercase = text.lower()

    for character in text_lowercase:
        if not character.isalpha():
            continue

        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1

    return characters


def sort_on(dict):
    return dict["num"]


def converto_to_list_of_dict(dict):
    new_list = []
    for key, value in dict.items():
        new_list.append({"char": key, "num": value})
    return new_list


main()
