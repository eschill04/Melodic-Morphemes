import pandas as pd
import nltk
from nltk.corpus import stopwords


# Download the set of stop words
stop_words = set(stopwords.words('english'))

df = pd.read_csv("songs.csv")
# NEED TO STRIP PUNCTUATION
 
# Extract list of song lyrics for each genre
# make a list of lyrics by genre
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
    n = 1
    ngrams = []
    for lyric in lyrics:
        if type(lyric) != float:
            words = lyric.split()
            # remove any words that contain ] or [
            words = [word.lower() for word in words if "]" not in word and "[" not in word]
            #words = [word for word in words if word.lower() not in stop_words.union({"•", "-", "&"})]
            contractions = [word for word in ngrams if word[0] == "'"]
            for i in range(len(words) - n + 1):
                ngram = " ".join(words[i:i+n])
                ngrams.append(ngram)
    
    # Count frequency of n-grams
    print("\n")
    print("Genre: ", genre)
    ngram_counts = pd.Series(ngrams).value_counts()
    
    # # notes
    # ain't, don't, doesn't
    if "ain't" in ngram_counts:
        print("ain't: ", ngram_counts["ain't"])
    if "don't" in ngram_counts:
        print("don't: ", ngram_counts["don't"])
    if "doesn't" in ngram_counts:
        print("doesn't: ", ngram_counts["doesn't"])

    #look at frequency of contractions: print count of words with apostrophes
    # print("Contractions: ", len(contractions), pd.Series(contractions).value_counts()[:20])

    #print("Top 20 1-grams: ", ngram_counts.head(20))

    # print("Swear words: ")
    # for word in ["bitch", "dick", "fuck", "pussy", "shit", "bastard", "ass", "booty"]:
    #     try:
    #         print(word,":", ngram_counts[word])
    #     except KeyError:
    #         pass

    n = 2
    ngrams = []
    dups = set()
    he_she_it_dont = set()
    he_she_it_doesnt = set()
    for lyric in lyrics:
        if type(lyric) != float:
            words = lyric.split()
            # remove any words that contain ] or [
            words = [word.lower() for word in words if "]" not in word and "[" not in word]
            for i in range(len(words) - n + 1):
                if words[i] in set(["he", "she", "it", "that", "this"]):
                    if words[i+1] == "don't":
                        he_she_it_dont.add(" ".join(words[i:i+2]))
                    elif words[i+1] == "doesn't":
                        he_she_it_doesnt.add(" ".join(words[i:i+2]))  

            #words = [word for word in words if word.lower() not in stop_words.union({"•", "-", "&"})]
            for i in range(len(words) - n + 1):
                if words[i] == words[i+1]:
                    dups.add(words[i])
    # # look at frequency of reduplication (n = 2)
    # print("Doesn't Count", len(he_she_it_doesnt), he_she_it_doesnt)
    # print("Don't Count", len(he_she_it_dont), he_she_it_dont)
    # print("Reduplication:", len(dups))
    # print(dups)

    n = 3
    ngrams = []
    verbs = set()
    for lyric in lyrics:
        if type(lyric) != float:
            words = lyric.split()
            # remove any words that contain ] or [
            words = [word.lower() for word in words if "]" not in word and "[" not in word]
            #words = [word for word in words if word.lower() not in stop_words.union({"•", "-", "&"})]
            for i in range(len(words) - n + 1):
                if "don't" == words[i] or "ain't" == words[i] or "can't" == words[i] or "doesn't" == words[i]:
                    verbs.add(" ".join(words[i:i+3]))
    print(verbs)
    
