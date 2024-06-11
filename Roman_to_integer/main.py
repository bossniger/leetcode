def roman_to_arabic(roman_number):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_number = 0
    prev_value = 0

    for i in range(len(roman_number)-1, -1, -1):
        current_value = roman_dict[roman_number[i]]
        if current_value < prev_value:
            arabic_number -= current_value
        else:
            arabic_number += current_value
        prev_value = current_value
    return arabic_number


roman_number = input("Введите римское число: ")
arabic_number = roman_to_arabic(roman_number)
print(arabic_number)