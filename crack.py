
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

print(k4_partial_layout)

# im thinking maybe we replace 
# EAST with KITA
# NORTH with (KOREA)? or maybe (TOZAI)
# EAST with KITA (again)
# CLOCK to (TOKEI)?

# basically, we can define the cipher key with the alignemnt

# draw a circle graph using networkx. let's have the characters