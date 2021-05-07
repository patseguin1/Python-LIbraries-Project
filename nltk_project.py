import nltk

# Grab the movie reviews and state of the union corpus for analyzing
text = nltk.Text(nltk.corpus.state_union.words())
text_2 = nltk.Text(nltk.corpus.movie_reviews.words())

# Print and plot the 25 most used words from the corpus
fd = text.vocab()
fd.tabulate(25)
fd.plot(25)

fd_2 = text_2.vocab()
fd_2.tabulate(25)
fd_2.plot(25)
