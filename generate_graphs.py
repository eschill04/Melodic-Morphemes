import matplotlib.pyplot as plt
import numpy as np

def aphaeresis():
    # Bar chart with number of instances of "'till", "'bout", "'cause", "'em", "'round"
    # in Genres Pop, Country, RnB, Rock
    genres = ['Country', 'Pop', 'RnB', 'Rock']
    contractions = ["'till", "'bout", "'cause", "'em", "'round", "Other"]
    #data_dict = {'Country': [6, 40, 63, 12, 16], 'Pop': [31, 11, 1, 1, 26], 'RnB': [8, 15, 49, 7, 1], 'Rock': [3, 5, 15, 4, 2]}
    inverse_data = {"'till": [6, 31, 8, 3], "'bout": [40, 11, 15, 5], "'cause": [63, 1, 49, 15], "'em": [12, 1, 7, 4], "'round": [16, 26, 1, 2], "Other": [4, 3, 4, 0]}

    # show bar graph where each bar is one genre, and is composed of the percentage of each contraction it has
    fig, ax = plt.subplots()
    heights = np.asarray([0, 0, 0, 0])
    x = range(len(genres))
    colors=['darkorange', 'black', 'peachpuff', 'chocolate', 'dimgray', 'gainsboro']
    for i, contract in enumerate(contractions):
        # set color to be black, light orange, dark orange, light gray, dark gray
        ax.bar(x, inverse_data[contract], bottom=heights, label=contract, color = colors[i])
        heights += np.asarray(inverse_data[contract])
    ax.set_xticks([pos for pos in x])
    ax.set_xticklabels(genres)
    ax.set_xlabel("Genre")
    ax.set_ylabel("Frequency")
    ax.set_title("Use of aphaeresis in different genres")
    ax.legend()
    plt.show()

def reduplication():
    genres = ["Country", "Pop", "R&B", "Rock"]
    numbers = [24, 53, 50, 31]
    fig, ax = plt.subplots()
    colors=['black', 'peachpuff', 'chocolate', 'dimgray']

    # make a bar chart horizontal
    ax.barh(genres, numbers, color=colors)
    # include the numbers themselves
    for i in range(len(numbers)):
        ax.text(numbers[i], i, numbers[i], ha='left', va='center')
    ax.set_xlabel("Number of unique reduplicated words")
    ax.set_ylabel("Genre")
    ax.set_title("Reduplication in different genres")
    plt.show()

    
def aint_dont_doesnt():
    genres = ['Country', 'Pop', 'RnB', 'Rock']
    data_dict = {'Country': [93, 96, 0], 'Pop': [12, 152, 13], 'RnB': [64, 134, 0], 'Rock': [3, 115, 4]}
    fig, axs = plt.subplots(1, 4, figsize=(15, 4))  # Adjusted figsize for better visibility
    colors = ['peachpuff', 'chocolate', 'black']
    labels = ["ain't", "don't", "doesn't"]

    # Define a custom autopct function that includes both percentage and actual number
    def custom_autopct(pct, allvals):
        total = sum(allvals)
        val = int(round(pct*total/100.0))
        if val != 0:  # To prevent showing 0 values
            return "{v:d}".format(v=val)
        else:
            return ""

    for i, genre in enumerate(genres):  
        wedges, texts, autotexts = axs[i].pie(data_dict[genre], colors=colors, autopct=lambda pct: custom_autopct(pct, data_dict[genre]),
                                              textprops=dict(color="white"), pctdistance=0.75)  # Default text color
        axs[i].set_title(genre)

        colorlist = ["black", "black", "white"]
        for autotext, color in zip(autotexts, colorlist):
            autotext.set_color(color)

    # Handling the legend: Show one legend for all charts
    fig.legend(wedges, labels, loc="center right", title="Expressions")
    plt.subplots_adjust(right=0.9)  # Adjust subplot to fit the legend on the right
    plt.suptitle("Use of 'ain't', 'don't', 'doesn't' in different genres")
    plt.show()

def doubleneg():
    genres = ["Country", "Pop", "R&B", "Rock"]
    numbers = [16, 7, 23, 0]
    fig, ax = plt.subplots()
    colors=['black', 'peachpuff', 'chocolate', 'dimgray']

    # make a bar chart horizontal
    ax.barh(genres, numbers, color=colors)
    # include the numbers themselves
    for i in range(len(numbers)):
        ax.text(numbers[i], i, numbers[i], ha='left', va='center')
    ax.set_xlabel("Number of unique (3-gram) phrases using double negatives")
    ax.set_ylabel("Genre")
    ax.set_title("Unique instances of double negation in different genres")
    plt.show()
    
doubleneg()

