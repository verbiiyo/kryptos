from typing import List, Tuple

from crack import vigenere_decipher, wrap_decipher, multi_wrap_decipher, K1_SOLVED, K2_SOLVED, K3_SOLVED
from messages import KRYPTOS, K1, K2, K3, K4, K4_WITH_HINTS


def get_hint_chars() -> Tuple[List[int], List[str], List[str]]:
    indices = []
    k4_chars = []
    hint_chars = []

    # oh, also, there are some places where they do match...
    # so for those, we will automatically add them as well.
    matching_char_indices = [32, 73]

    # let's print the mismatch characters and their indices
    for i, (k4_char, k4_hint_char) in enumerate(zip(K4, K4_WITH_HINTS)):
        if k4_char != k4_hint_char or i in matching_char_indices:
            indices.append(i)
            k4_chars.append(k4_char)
            hint_chars.append(k4_hint_char)

    return indices, k4_chars, hint_chars


def try_all_possible_berlin_clock_combinations():
    for i in range(2):
        for j in range(5):
            for k in range(12):
                for l in range(5):
                    print("Trying", i, j, k, l)
                    multi_wrap_decipher(K4, [i, j, k, l])


if __name__ == "__main__":
    hint_indices, no_hint_chars, hint_chars = get_hint_chars()
    print(f"Indices:\t{" ".join([str(i) for i in hint_indices])}")
    print(f"K4 Chars:\t{"  ".join(no_hint_chars)}")
    print(f"Hint Chars:\t{"  ".join(hint_chars)}")

    try_all_possible_berlin_clock_combinations()

    # for i in range(100):
    #     for j in range(100):
    #         for k in range(100):
    #             print("Trying", i, j, k)
    #             multi_wrap_decipher(K4, [i, j, k])