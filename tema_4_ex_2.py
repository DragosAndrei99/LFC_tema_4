import re

def count_words_with_even_as(filename):
    with open(filename, 'r') as file:
        words = file.read().split()

    even_a_count = sum(1 for word in words if re.match(r'^(aa)+[^a]+.*$', word))
    return even_a_count

def replace_b_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()

    modified_words = [str(len(word)) if re.match(r'^b.*b$', word) else word for word in words]
    result_text = ' '.join(modified_words)

    with open(filename, 'w') as file:
        file.write(result_text)

def concatenate_invalid_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()

    valid_letters = re.compile(r'^[a|b|c|d]+$')
    invalid_words = [word for word in words if not valid_letters.match(word)]
    concatenated_invalid = ''.join(invalid_words)

    return concatenated_invalid

if __name__ == '__main__':
    # Test:
    filename = 'input_tema_4.txt'

    # Task a. - Să se verifice câte cuvinte au un număr par de “a”-uri la început
    even_a_count = count_words_with_even_as(filename)
    print(f"Number of words with an even number of 'a's in the beginning: {even_a_count}")

    # Task b. Să se înlocuiască fiecare cuvânt care începe și se temină cu “b” cu lungimea lui.
    replace_b_words(filename)

    # Task c. Să se concateneze toate cuvintele invalide (nu sunt cuvinte peste vocabularul dat) din fișier, dacă există
    concatenated_invalid = concatenate_invalid_words(filename)
    print(f"Concatenated invalid words: {concatenated_invalid}")
