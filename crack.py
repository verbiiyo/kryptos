
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
    out_str = "\n".join([out_str[i:i+31] for i in range(0, len(out_str), 31)])

    return out_str


def vigenere_decipher(text: str, key1: str, key2: str):
    # first key is used to construct the vigenere table
    # vigenere table is where you take the key1 and pull it all to the beginning
    # of the standard 26 letter alphabet.

    # then, key2 can decipher the text using the vigenere table
    # by finding the row of the key2 character and the column of the text character

    # let's begin
    # first, construct the vigenere table
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = ""

    for char in key1:
        table += char
        alphabet = alphabet.replace(char, "")

    table += alphabet

    print(table)

    exit()




print(f"K1 has {len(K1.replace('\n', ''))} characters")
print(f"K2 has {len(K2.replace('\n', ''))} characters")
print(f"K3 has {len(K3.replace('\n', ''))} characters")
print(f"K4 has {len(K4.replace('\n', ''))} characters")
print()

print("K1 decrypted:")
print(vigenere_decipher(K1, "KRYPTOS", "PALIMPSEST"))


# we can decrypt K3 with wrap decypher using 192 as the key
print("K3 decrypted:")
print(wrap_decypher(K3, 192))
# print(f"K3 has {len(K3.replace('\n', ''))} characters")

print("-----")

print(K4)
print(len(K4.replace("\n", "")))

# print(wrap_decypher(K1, 192))