import string

def analyze_string(input_str):
    words = input_str.split()
    word_count = len(words)
    letter_count = sum(c.isalpha() for c in input_str)
    digit_count = sum(c.isdigit() for c in input_str)

    letter_freq = {letter: input_str.count(letter) for letter in string.ascii_letters}
    digit_freq = {digit: input_str.count(digit) for digit in string.digits}

    print(f"Ilość słów: {word_count}")
    print(f"Ilość liter: {letter_count}")
    print(f"Ilość cyfr: {digit_count}")
    print("Statystyka częstości występowania liter:")
    for letter, freq in letter_freq.items():
        if freq > 0:
            print(f"{letter}: {freq}")
    print("Statystyka częstości występowania cyfr:")
    for digit, freq in digit_freq.items():
        if freq > 0:
            print(f"{digit}: {freq}")

def main():
    input_str = input("Podaj łańcuch znaków: ")
    analyze_string(input_str)

if __name__ == "__main__":
    main()
