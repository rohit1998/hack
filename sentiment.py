from nltk.sentiment.vader import SentimentIntensityAnalyzer

with open("comments") as f:
	t = f.read().split('\n\n\n\n\n')

sid = SentimentIntensityAnalyzer()

for sentence in t:
	ss = sid.polarity_scores(sentence)
	print(sentence,ss['pos'])