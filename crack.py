
# from coded import k4_no_spaces, k4_unsolved, clock_forward

# print(k4_no_spaces)

# print(clock_forward(k4_no_spaces, depth=1))

from messages import KRYPTOS, K1, K2, K3, K4


# create a decorator that we can use to wrap all of these functions to flag any solutions that we find
# with certain keywords

KEYWORDS = ["CLOCK", "BERLIN", "EAST", "NORTH"]

def flag_solution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if any(keyword in result for keyword in KEYWORDS):
            print("FOUND!", result)
            exit()

        return result
    return wrapper


# apparently K3 can be decrypted with 192 characters

# let's gather the 192nd character from K3 for the full sequence
@flag_solution
def wrap_decypher(text: str, wrap_key: int):
    cypher_text = text.replace(" ", "").replace("\n", "")

    out_str = ""
    for i in range(len(cypher_text)):
        char_index = wrap_key * (i + 1)
        out_str += cypher_text[char_index % len(cypher_text)]

    # re-organize out_str to match K3's newline format
    # out_str = "\n".join([out_str[i:i+31] for i in range(0, len(out_str), 31)])

    return out_str


@flag_solution
def vigenere_decipher(cipher_text: str, alphabet_key: str, main_key: str):
    # first key is used to construct the Vigenère table
    # Vigenère table is where you take key1 and pull it all to the beginning
    # of the standard 26-letter alphabet, excluding the '?' character.

    # Interestingly enough, when you include the `?` character in the alphabet, it only
    # partially decrypts the text. So they deliberately left ? as a special ommitted character.

    cipher_text = cipher_text.replace("\n", "")

    # construct the Vigenère table (exclude '?')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = ""
    for char in alphabet_key:
        if char not in table:
            table += char
            alphabet = alphabet.replace(char, "")
    table += alphabet

    # prepare to hold deciphered output
    out_str = ""

    # track positions in the key2 string, since it needs to ignore '?' in cipher text
    key2_index = 0

    # loop through each character of the cipher text
    for i, cipher_char in enumerate(cipher_text):
        if cipher_char == "?":
            # leave question marks unchanged
            out_str += "?"
        else:
            # get the index of the cipher character in the table
            cipher_index = table.index(cipher_char)

            # get the corresponding key2 character (skip over '?' in key2)
            key2_char = main_key[key2_index % len(main_key)]
            key2_index += 1

            # get the index of the key2 character in the table
            key2_index_in_table = table.index(key2_char)

            # decipher by subtracting the key2 index from the cipher text index (mod table length)
            decipher_index = (cipher_index - key2_index_in_table) % len(table)

            # append the deciphered character to the output
            out_str += table[decipher_index]
    
    return out_str


@flag_solution
def multi_wrap_decipher(text: str, wraps: list):
    # wrap the text multiple times
    for wrap in wraps:
        text = wrap_decypher(text, wrap)
    return text


print(f"K1 has {len(K1.replace('\n', ''))} characters")
print(f"K2 has {len(K2.replace('\n', ''))} characters")
print(f"K3 has {len(K3.replace('\n', ''))} characters")
print(f"K4 has {len(K4.replace('\n', ''))} characters")
print()

# print("K1 Decrypted:")
# print(vigenere_decipher(K1, "KRYPTOS", "PALIMPSEST"))
# print()

# print("K2 Decrypted:")
# print(vigenere_decipher(K2, "KRYPTOS", "ABSCISSA"))
# print()

# # we can decrypt K3 with wrap decypher using 192 as the key
# print("K3 Decrypted:")
# print(wrap_decypher(K3, 192))  # where the flip does 192 come from?
# print()

print("K4 Decrypted...???:")
# print(multi_wrap_decipher(K4, [1, 4, 4, 11, 4]))  # berlin square counts
# print(multi_wrap_decipher(K4, [1, 2, 11, 1]))  # clock screen shot time (10:31)
# print(multi_wrap_decipher(K4, [11, 2, 1, 3]))  # berlin clock minutes filled?
# print(multi_wrap_decipher(K4, [2, 4, 11, 2, 1, 1, 3]))  # berlin with degrees as hours?
# print(multi_wrap_decipher(K4, [17, 6, 1975]))  # berlin clock date created?
# print(multi_wrap_decipher(K4, [17, 6, 1975]))  # berlin clock date created?
# print(vigenere_decipher(K4, "KRYPTOS", "CLOCK"))
# print(vigenere_decipher(K4, "KRYPTOS", "MENGENLEHREUHR"))  # clock name
# print(vigenere_decipher(K4, "KRYPTOS", "BERLINUHR"))  # clock name
# print(vigenere_decipher(wrap_decypher(K4, 192), "KRYPTOS", "GWMP"))#, "KRYPTOS", "PALIMPSEST"))

# print(multi_wrap_decipher(K4, [8, 31]))
# print(multi_wrap_decipher(K4, [31, 8]))


# lets try setting the wrap decipher key to the ascii values of the characters in "KRYPTOS"
print(multi_wrap_decipher(K4, [ord(char) for char in "KRYPTOS"]))


# japanese stuff
# print(vigenere_decipher(K4, "KRYPTOS", "TOZAI"))
# print(vigenere_decipher(K4, "KRYPTOS", "KITA"))
# print(vigenere_decipher(K4, "KRYPTOS", "HIGASHI"))
# print(vigenere_decipher(K4, "KRYPTOS", "TOKYO" ))

# print(wrap_decypher(K4, -336))  # berlin square counts


# for i in reversed([1, 4, 4, 11, 4]):
# for i in reversed([4, 4, 4, 4, 4, 4]):
    # print(wrap_decypher(K4, i))

# BRO... doing this results in a matrix-like output that has some very interesting patterns
# like the boundary of repeating "O"s on the end and bottom of the matrix
# and the repeating as you go further in the i dimension.
# for i in range(1, 120):
#     # txt = vigenere_decipher(vigenere_decipher(wrap_decypher(K4, i), "KRYPTOS", "ABSCISSA"), "KRYPTOS", "PALIMPSEST")
#     # if "EAST" in txt:
#         # print(txt)

#     nums = list(range(1, i))

#     txt = multi_wrap_decipher(K4, [x ** 2 for x in nums])
#     print(txt)

#     if "EAST" in txt:
#         print("FOUND!")
#         exit()


# for i in range(1, 100):
#     # txt = vigenere_decipher(vigenere_decipher(wrap_decypher(K4, i), "KRYPTOS", "ABSCISSA"), "KRYPTOS", "PALIMPSEST")
#     # if "EAST" in txt:
#         # print(txt)

#     txt = multi_wrap_decipher(K4, [(x % i) for x in [1, 4, 4, 11, 4]])
#     print(txt)

#     if "EAST" in txt:
#         print("FOUND!")
#         exit()
