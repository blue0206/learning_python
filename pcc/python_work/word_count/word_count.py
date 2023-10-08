from pathlib import Path

intro = "This program determines how many times a certain word appears in each "
intro += "of the following texts:\n"
intro += "\tThe Great Gatsby\n\tSherlock Holmes\n"
intro += "\tAnna Karenina\n\tRomeo and Juliet\n"
print(intro)

path_gatsby = Path("word_count/the_great_gatsby.txt")
path_sherlock = Path("word_count/sherlock_holmes.txt")
path_karenina = Path("word_count/anna_karenina.txt")
path_romeo = Path("word_count/romeo_and_juliet.txt")

print("Enter a word to know how many time it appears in the texts.")
print("Simply press enter to exit.")

while True:
    word = input("Enter a word: ")

    if word == '':
        break

    try:
        gatsby = path_gatsby.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        count_gatsby = gatsby.lower().count(f" {word} ")
        print(f"The Great Gatsby has {count_gatsby} occurrences of '{word}'.")

    try:
        sherlock = path_sherlock.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        count_sherlock = sherlock.lower().count(f" {word} ")
        print(f"Sherlock Holmes has {count_sherlock} occurrences of '{word}'.")

    try:
        karenina = path_karenina.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        count_karenina = karenina.lower().count(f" {word} ")
        print(f"Anna Karenina has {count_karenina} occurrences of '{word}'.")

    try:
        romeo = path_romeo.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        count_romeo = romeo.lower().count(f" {word} ")
        print(f"Romeo and Juliet has {count_romeo} occurrences of '{word}'.")