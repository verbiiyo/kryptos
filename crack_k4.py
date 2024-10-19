from typing import List, Tuple

from crack import vigenere_decipher, wrap_decipher, multi_wrap_decipher, K1_SOLVED, K2_SOLVED, K3_SOLVED
from messages import KRYPTOS, K1, K2, K3, K4, K4_WITH_HINTS
import numpy as np


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



def modular_distance(a: str, b: str) -> float:
    a_values = np.array([ord(c) for c in a])
    b_values = np.array([ord(c) for c in b])

    # get min_n which is the min value out of all a and b value arrays
    min_n = min(np.min(a_values), np.min(b_values))

    # convert a and b to start at 0
    a_values -= min_n
    b_values -= min_n

    # get n which is max value out of all a and b value arrays
    n = max(np.max(a_values), np.max(b_values)) + 1

    mod_dist = np.abs(a_values - b_values)
    mod_dist = np.minimum(mod_dist, n - mod_dist)
    mod_dist = mod_dist.astype(float)

    return np.mean(mod_dist)


def cost(decipher_attempt_text: str) -> float:
    return modular_distance(K4, decipher_attempt_text)




if __name__ == "__main__":
    hint_indices, no_hint_chars, hint_chars = get_hint_chars()
    print(f"Indices:\t{" ".join([str(i) for i in hint_indices])}")
    print(f"K4 Chars:\t{"  ".join(no_hint_chars)}")
    print(f"Hint Chars:\t{"  ".join(hint_chars)}")

    assert cost(K4) == 0.0
    assert cost(K4_WITH_HINTS) == 1.3814432989690721

    print(cost(K4_WITH_HINTS))

    # WORDS = ["WEST", "SOUTH", "WESTERN", "PARIS", "TOWER", "NORTHWEST", "MOSCOW", "COMPASS", "TIMELINE", "WATCH"]
    # for word in WORDS:
    #     print(vigenere_decipher(K4, "KRYPTOS", word))


    # try_all_possible_berlin_clock_combinations()
    # for i in range(100):
    #     for j in range(100):
    #         for k in range(100):
    #             print("Trying", i, j, k)
    #             multi_wrap_decipher(K4, [i, j, k])