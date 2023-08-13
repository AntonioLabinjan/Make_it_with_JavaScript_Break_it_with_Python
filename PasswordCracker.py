import itertools

lower_chars = "qwertzuiopasdfghjklyxcvbnm"
upper_chars = "QWERTZUIOPASDFGHJKLYXCVBNM"
all_numbers = "2431509876"
all_symbols = "~!@#$%^&*"

def generate_possible_characters(allowed_chars):
    possible_chars = ""
    if 'l' in allowed_chars:
        possible_chars += lower_chars
    if 'u' in allowed_chars:
        possible_chars += upper_chars
    if 'n' in allowed_chars:
        possible_chars += all_numbers
    if 's' in allowed_chars:
        possible_chars += all_symbols
    return possible_chars

def list_combinations_with_exact_length(allowed_chars, length):
    possible_chars = generate_possible_characters(allowed_chars)
    for combination in itertools.product(possible_chars, repeat=length):
        yield ''.join(combination)

allowed_chars = input("Karakteristike lozinke (l - mala slova, u - velika slova, n - brojevi, s - simboli): ")
length = int(input("Unesite duljinu lozinke: "))

for password in list_combinations_with_exact_length(allowed_chars, length):
    print(password)

input("Pritisnite enter za zatvaranje prozora...")