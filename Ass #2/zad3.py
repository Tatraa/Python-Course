def roman_to_arabic(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic = 0
    prev_value = 0
    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        arabic += value if value >= prev_value else -value
        prev_value = value
    return arabic

def arabic_to_roman(arabic):
    roman_numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                      100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman = ''
    for value in sorted(roman_numerals.keys(), reverse=True):
        while arabic >= value:
            roman += roman_numerals[value]
            arabic -= value
    return roman

def is_valid_roman(roman):
    valid_chars = "IVXLCDM"
    if any(char not in valid_chars for char in roman):
        return False
    if "IIII" in roman or "VV" in roman or "XXXX" in roman or "LL" in roman or "CCCC" in roman or "DD" in roman or "MMMM" in roman:
        return False
    if any(roman.count(char) > 3 for char in "IVXLCDM"):
        return False
    return True

def main():
    input_str = input("Podaj liczbę rzymską lub arabską: ")
    try:
        if input_str.isdigit():
            arabic = int(input_str)
            if 1 <= arabic <= 3999:
                roman = arabic_to_roman(arabic)
                print(f"Liczba rzymska: {roman}")
            else:
                print("Liczba arabska musi być w zakresie 1-3999.")
        elif is_valid_roman(input_str):
            arabic = roman_to_arabic(input_str)
            print(f"Liczba arabska: {arabic}")
        else:
            print("Nieprawidłowy format liczby rzymskiej.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()
