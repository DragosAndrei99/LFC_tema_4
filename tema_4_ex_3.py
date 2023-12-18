import re

def check_string_conditions(input_string):
    char_pattern = re.compile(r'[#$%]')

    capital_letter_pattern = re.compile(r'[A-Z]')

    length_pattern = re.compile(r'.{10,}')

    digits_pattern = re.compile(r'\d{2,}')

    conditions_met = (
        char_pattern.search(input_string) is not None and
        capital_letter_pattern.search(input_string) is not None and
        length_pattern.match(input_string) is not None and
        digits_pattern.search(input_string) is not None
    )

    return conditions_met

# Test:
example_strings = ["Abc#1234", "NoSpecialChars", "Short#Pwd", "$ecretP@ssword", "AbCdEfG$12"]
for string in example_strings:
    result = check_string_conditions(string)
    print(f"{string}: {'Valid' if result else 'Invalid'}")
