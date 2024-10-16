
k4_unsolved = """
                           OBKR
UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO
TWTQSJQSSEKZZWATJKLUDIAWINFBNYP
VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR
"""  # maybe the `?` pre-pends the key?

k4_partial = "?OBKRUOXOGHULBSOLIFBBWEASTNORTHEASTOTWTQSJQSSEKZZWATJKLUDIAWINFBBERLINMZFPKWGDKZXTJCDIGKUHUAUEKCAR"

# same text but laid out like the video https://www.youtube.com/watch?v=jVpsLMCIB0Y
k4_partial_layout = """
                          ?OBKR
UOXOGHULBSOLIFBBWEASTNORTHEASTO
TWTQSJQSSEKZZWATJKLUDIAWINFBBER
LINMZFPKWGDKZXTJCDIGKUHUAUEKCAR
"""

k4_clock_layout = """
                          ?OBKR
UOXOGHULBSOLIFBBWEASTNORTHEASTO
TWTQSJQSSEKZZWATJKLUDIAWINFBBER
LINCLOCKWGDKZXTJCDIGKUHUAUEKCAR
"""  # MZFPK gets mapped to CLOCK (hint from Jim Sanborn)

print(k4_unsolved)

# im thinking maybe we replace 
# EAST with KITA
# NORTH with (KOREA)? or maybe (TOZAI)
# EAST with KITA (again)
# CLOCK to (TOKEI)?

# basically, we can define the cipher key with the alignemnt

# draw a circle graph using networkx. let's have the characters


def plot_characters_in_cirlce(text: str, clockwise: bool = True):
    # plot all circles in a perfect circle equidistent from each other along
    # the perimeter.

    # the first character begins at the top of the circle at
    # 0 degrees aka (0, 1) on the unit circle. the next character is
    # 360/len(text) degrees away from the previous character.
    # and so on.

    # if clockwise is False, then the characters are plotted in the reverse
    # direction.

    # TODO:
    pass


k4_no_spaces = k4_unsolved.replace(" ", "").replace("\n", "")
plot_characters_in_cirlce(k4_no_spaces, clockwise=True)