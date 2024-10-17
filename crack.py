
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


# we can decrypt K3 with wrap decypher using 192 as the key
print("K3 decrypted:")
print(wrap_decypher(K3, 192))

print("-----")

print(K4)
print(len(K4.replace("\n", "")))

# print(wrap_decypher(K1, 192))