import lyricsgenius
import pandas as pd

client_id = 'qV1NAhgDyrjKtysnG7n3ekxuT_a2BD_KYfhnyx_e32rvOgDgSyH0b3vD56tZbYgA'
client_secret = '8emr36hq8ZdqNLQLPLw3-4d5hb_7IoKWCusTeImbJc5znf9OzMmczmRYnYBAIk5EqG2CrCakaehID0gZuaDLMQ'

genius = lyricsgenius.Genius(client_id, client_secret)

df = pd.read_csv('songs.csv')
for i, row in df.iterrows():
    if row['genre'] == 'Rock':
        # filter out songs in this list: popular, fly girl, white crocs, feelings, waiting for you, think fast,
        # 2 sugar, i remember everything, fantasy, we go down together, what was i made for, dance the night

        remove_list = ["popular", "fly girl", "white crocs", "feelings", "waiting for you", "think fast", "2 sugar",
                        "i remember everything", "fantasy", "we go down together", "what was i made for", "dance the night"]
        if any(word in row['track'].lower() for word in remove_list):
            df = df.drop(i)
            continue
        song = genius.search_song(row['track'], row['artist'])
        if song:
            df.loc[i, 'lyrics'] = song.lyrics
        else:
            # remove the song from the dataframe
            df = df.drop(i)
            print("could not find oopsies, sorry", row['track'], row['artist'])

df.to_csv('songs.csv', index=False)