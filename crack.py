
# from coded import k4_no_spaces, k4_unsolved, clock_forward

# print(k4_no_spaces)

# print(clock_forward(k4_no_spaces, depth=1))

from messages import KRYPTOS, K1, K2, K3, K4


# apparently K3 can be decrypted with 192 characters

# let's gather the 192nd character from K3 for the full sequence
def wrap_decypher(text: str, wrap_key: int):
    cypher_text = text.replace(" ", "").replace("\n", "")

    out_str = ""
    for i in range(len(cypher_text)):
        char_index = wrap_key * (i + 1)
        out_str += cypher_text[char_index % len(cypher_text)]

    # re-organize out_str to match K3's newline format
    # out_str = "\n".join([out_str[i:i+31] for i in range(0, len(out_str), 31)])

    return out_str


def vigenere_decipher(cipher_text: str, key1: str, key2: str):
    # first key is used to construct the Vigenère table
    # Vigenère table is where you take key1 and pull it all to the beginning
    # of the standard 26-letter alphabet, excluding the '?' character.

    # Interestingly enough, when you include the `?` character in the alphabet, it only
    # partially decrypts the text. So they deliberately left ? as a special ommitted character.

    cipher_text = cipher_text.replace("\n", "")

    # construct the Vigenère table (exclude '?')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = ""
    for char in key1:
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
            key2_char = key2[key2_index % len(key2)]
            key2_index += 1

            # get the index of the key2 character in the table
            key2_index_in_table = table.index(key2_char)

            # decipher by subtracting the key2 index from the cipher text index (mod table length)
            decipher_index = (cipher_index - key2_index_in_table) % len(table)

            # append the deciphered character to the output
            out_str += table[decipher_index]
    
    return out_str





print(f"K1 has {len(K1.replace('\n', ''))} characters")
print(f"K2 has {len(K2.replace('\n', ''))} characters")
print(f"K3 has {len(K3.replace('\n', ''))} characters")
print(f"K4 has {len(K4.replace('\n', ''))} characters")
print()

print("K1 Decrypted:")
print(vigenere_decipher(K1, "KRYPTOS", "PALIMPSEST"))
print()

print("K2 Decrypted:")
print(vigenere_decipher(K2, "KRYPTOS", "ABSCISSA"))
print()


# we can decrypt K3 with wrap decypher using 192 as the key
print("K3 Decrypted:")
print(wrap_decypher(K3, 192))
print()

# print("-----")

# print(K4)
# print(len(K4.replace("\n", "")))

# print(wrap_decypher(K1, 192))