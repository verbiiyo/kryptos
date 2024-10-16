import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

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
    n = len(text)

    # Create a graph
    G = nx.Graph()

    # Add nodes for each character in the text
    for i, char in enumerate(text):
        G.add_node(i, label=char)

    # Calculate angles between characters (in radians)
    angle_step = 2 * np.pi / n
    if not clockwise:
        angle_step = -angle_step

    # Calculate positions for each character around the circle
    pos = {}
    for i in range(n):
        angle = i * angle_step
        x = np.sin(angle)
        y = np.cos(angle)
        pos[i] = (x, y)

    # Draw the graph
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')

    # Draw the nodes (characters)
    nx.draw(G, pos, ax=ax, with_labels=False, node_size=0)  # No actual node circles

    # Annotate each node with the corresponding character
    for i, (x, y) in pos.items():
        char = G.nodes[i]['label']
        ax.text(x, y, char, fontsize=8, ha='center', va='center')

    # Plot the unit circle
    circle = plt.Circle((0, 0), 1, color='lightgray', fill=False)
    ax.add_artist(circle)

    # Set limits and remove axes
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')

    plt.show()
    plt.savefig("circle.png")


k4_no_spaces = k4_unsolved.replace(" ", "").replace("\n", "")
plot_characters_in_cirlce(k4_no_spaces, clockwise=True)