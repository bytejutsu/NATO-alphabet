import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_code = {row.letter: row.code for (index, row) in data.iterrows()}


def prompt():
    word = input("Enter Word: ").upper()
    try:
        result = [phonetic_code[letter] for letter in word]
    except KeyError:
        print("sorry only letters in the alphabet please")
        prompt()
    else:
        print(result)


prompt()


