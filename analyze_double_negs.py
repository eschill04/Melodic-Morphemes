import pandas as pd

double_negatives = {"ain't shit without", "can't nobody yeah", "don't feel no", "can't nobody stop", "don't have no", "don't want no", "ain't no bussin'"}
double_negatives2 = {"ain't nobody sellin'", "don't know nothin'", "ain't doin' jack", "don't mean nothin'", "ain't no tryin'", "don't want no", "can't drink no", "ain't nothin' but", "don't want none", "ain't got nothing", "ain't shit and", "ain't no thing", "ain't got nothin'", "ain't not around", "ain't nobody who", "ain't goin' nowhere"}
double_negatives3 = {"ain't no need", "ain't never been", "ain't no way", "ain't never seen", "ain't have shit", 'ain\'t no good"',"don't need nothin'", "ain't had nobody", "ain't no virtue", "don't want no", "ain't no problem", "ain't takin' no", "ain't no clothes", "ain't have nobody", "don't need no", "ain't nothing changed", "ain't got nothin'", "don't got nobody", "can't get no", "don't show no", "ain't no price", "ain't fight no", "can't take no"}


df = pd.read_csv('songs.csv')

genres = df["genre"].unique()
genre_lyrics = {}
for genre in genres:
    genre_lyrics[genre] = df[df["genre"] == genre]["lyrics"].tolist()

# for each item in lyrics, remove all words prior to the phrase "Lyrics"
for genre in genre_lyrics:
    lyrics = genre_lyrics[genre]

    for i in range(len(lyrics)):
        # if lyrics[i] is not a float (i.e. it is a string)
        if type(lyrics[i]) != float:
            lyrics[i] = lyrics[i].split("Lyrics")[1]

            # Remove all punctuation    
            lyrics[i] = lyrics[i].replace(",", "")
            lyrics[i] = lyrics[i].replace(".", "")
            lyrics[i] = lyrics[i].replace("!", "")
            lyrics[i] = lyrics[i].replace("?", "")
            lyrics[i] = lyrics[i].replace("(", "")
            lyrics[i] = lyrics[i].replace(")", "")
    
    # Tokenize lyrics into n-grams
    n = 3
    ngrams = []
    verbs = []
    for lyric in lyrics:
        if type(lyric) != float:
            words = lyric.split()
            # remove any words that contain ] or [
            words = [word.lower() for word in words if "]" not in word and "[" not in word]
            #words = [word for word in words if word.lower() not in stop_words.union({"•", "-", "&"})]
            for i in range(len(words) - n + 1):
                if " ".join(words[i:i+3]) in double_negatives or " ".join(words[i:i+3]) in double_negatives2 or " ".join(words[i:i+3]) in double_negatives3:
                    verbs.append(" ".join(words[i:i+3]))
    print(genre)
    print(verbs)


