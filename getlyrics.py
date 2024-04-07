import lyricsgenius
import pandas as pd

client_id = 'qV1NAhgDyrjKtysnG7n3ekxuT_a2BD_KYfhnyx_e32rvOgDgSyH0b3vD56tZbYgA'
client_secret = '8emr36hq8ZdqNLQLPLw3-4d5hb_7IoKWCusTeImbJc5znf9OzMmczmRYnYBAIk5EqG2CrCakaehID0gZuaDLMQ'

genius = lyricsgenius.Genius(client_id, client_secret)

df = pd.read_csv('songs.csv')
for i, row in df.iterrows():
    if row['genre'] == 'Country':
        song = genius.search_song(row['track'], row['artist'])
        if song:
            df.loc[i, 'lyrics'] = song.lyrics
        else:
            df.loc[i, 'lyrics'] = None
            print("could not find oopsies, sorry", row['track'], row['artist'])

df.to_csv('songs.csv', index=False)