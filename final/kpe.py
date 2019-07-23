from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import pke
import pdb
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


with open('./comments_f') as file:
	comments = file.read().split('\n\n\n\n')

with open("keyphrase",'w') as file:

	text = ""

	for comment in comments:

		# print(comment)

		try:
			extractor = pke.unsupervised.TopicRank()
			extractor.load_document(input=comment, language='en')
			extractor.candidate_selection()
			extractor.candidate_weighting()

			if comment.count(' ') <2:
				keyphrases = extractor.get_n_best(n=1)
			elif comment.count(' ') <4:
				keyphrases = extractor.get_n_best(n=2)
			elif comment.count(' ') <10:
				keyphrases = extractor.get_n_best(n=3)
			else:
				keyphrases = extractor.get_n_best(n=5)

			for key in keyphrases:
				file.write(key[0]+",")
			file.write('\n')
			
			# print(keyphrases,'\n\n')

			keyphrases =  [t[0].split(' ') for t in keyphrases]
			keyphrases = [item for sublist in keyphrases for item in sublist]


			if 'teams' in keyphrases and 'slack' not in keyphrases:
				# print(comment)
				ss = sid.polarity_scores(comment)
				print(ss)

				if(ss['pos']>0.2):
					text = text+comment

				if(ss['neg']>0.15):
					text = text+comment





				# sentiment = TextBlob(comment)
				# print("Sentiment Score: ", sentiment.sentiment.polarity)
			# if 'teams' not in keyphrases and 'slack' in keyphrases:
			# 	print(comment)
			# if 'teams' in keyphrases and 'slack' in keyphrases:
			# 	print(comment)


		except Exception as e: 
			# print(e)
			pass

	print(text)
	
	LANGUAGE = "english"
	SENTENCES_COUNT = 5

	parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))

	stemmer = Stemmer(LANGUAGE)

	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)


	print("#######")
	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		print(sentence)

		# print(keyphrases)