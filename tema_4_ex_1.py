import re

def check_number_type(input_string: str)-> str:
    float_pattern = re.compile(r'^[-+]?[0-9]*\.?[0-9]+$')
    integer_pattern = re.compile(r'^[-+]?[0-9]+$')
    if integer_pattern.match(input_string):
        return 'Numar intreg'
    elif float_pattern.match(input_string):
        return 'Numar real'
    else:
        return 'String-ul introdus nu este nici întreg, nici real'

# Test
input_str1 = "123"
input_str2 = "12.34"
input_str3 = "abc123"
input_str4 = "3.14abc"

print(check_number_type(input_str1)) # Numar intreg
print(check_number_type(input_str2)) # Numar real
print(check_number_type(input_str3)) # String-ul introdus nu este nici întreg, nici real
print(check_number_type(input_str4)) # String-ul introdus nu este nici întreg, nici real