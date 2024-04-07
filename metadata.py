import pandas as pd

# Print number of songs, number of artists, and number of genres
df = pd.read_csv('songs.csv')
print("Number of songs:", df['track'].nunique())
print("Number of artists:", df['artist'].nunique())
print("Number of genres:", df['genre'].nunique())

# average word count of lyrics
word_counts = df['lyrics'].str.split().str.len()
print("Average word count of lyrics:", word_counts.mean())