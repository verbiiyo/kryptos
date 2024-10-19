from typing import List, Tuple

from crack import vigenere_decipher, multi_wrap_decipher, wrap_decypher
from messages import KRYPTOS, K1, K2, K3, K4, K4_WITH_HINTS


def get_mismatch_chars() -> Tuple[List[int], List[str], List[str]]:
    indices = []
    k4_chars = []
    hint_chars = []

    # let's print the mismatch characters and their indices
    for i, (k4_char, k4_hint_char) in enumerate(zip(K4, K4_WITH_HINTS)):
        if k4_char != k4_hint_char:
            indices.append(i)
            k4_chars.append(k4_char)
            hint_chars.append(k4_hint_char)

    return indices, k4_chars, hint_chars

if __name__ == "__main__":
    mis_indices, mis_k4_chars, mis_hint_chars = get_mismatch_chars()
    print(f"Indices:\t{" ".join([str(i) for i in mis_indices])}")
    print(f"K4 Chars:\t{"".join(mis_k4_chars)}")
    print(f"Hint Chars:\t{"".join(mis_hint_chars)}")