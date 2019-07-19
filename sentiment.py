from nltk.sentiment.vader import SentimentIntensityAnalyzer

with open("comments2") as f:
	t = f.read().split('\n')

sid = SentimentIntensityAnalyzer()

for sentence in t:
	ss = sid.polarity_scores(sentence)
	print(sentence,ss['pos'])