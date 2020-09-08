NUMBERS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
NEGATIVE_PAIRS = {'V': 1, 'X': 1, 'L': 10, 'C': 10, 'D': 100, 'M': 100}


def roman_to_decimal(roman_number: str):
    decimal = 0
    previous_number = 1001
    previous_negative = False
    previous_counter = 0
    forbidden_number = 1001
    if not roman_number:
        return 'there is no number'
    for char in roman_number:
        if char in NUMBERS:
            if NUMBERS[char] < previous_number and NUMBERS[char] < forbidden_number:
                decimal += NUMBERS[char]
                previous_negative = False
                previous_counter = 0
            elif NUMBERS[char] == previous_number and previous_counter < 2 and not previous_negative and char not in \
                    ('V', 'L', 'D'):
                decimal += NUMBERS[char]
                previous_negative = False
                previous_counter += 1
            elif not previous_negative and previous_counter == 0 and NEGATIVE_PAIRS[char] == previous_number:
                decimal += NUMBERS[char] - previous_number * 2
                previous_counter = 0
                previous_negative = True
                forbidden_number = previous_number
            else:
                return 'not a valid Roman number'
        else:
            return 'not a valid Roman number'
        previous_number = NUMBERS[char]
    return decimal
