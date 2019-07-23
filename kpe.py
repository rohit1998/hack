import pke
import pdb
# initialize keyphrase extraction model, here TopicRank


# load the content of the document, here document is expected to be in raw
# format (i.e. a simple text file) and preprocessing is carried out using spacy
with open('./comments3') as f:
	comments = f.read().split('\n')

with open("keyphrase",'w') as file:

	for comment in comments:

		print(comment)
		# file.write("begin")
		try:
			extractor = pke.unsupervised.TopicRank()

			extractor.load_document(input=comment, language='en')

			# keyphrase candidate selection, in the case of TopicRank: sequences of nouns
			# and adjectives (i.e. `(Noun|Adj)*`)
			extractor.candidate_selection()

			# candidate weighting, in the case of TopicRank: using a random walk algorithm
			extractor.candidate_weighting()

		# N-best selection, keyphrases contains the 10 highest scored candidates as
		# (keyphrase, score) tuples
			if comment.count(' ') <2:
				keyphrases = extractor.get_n_best(n=1)
			elif comment.count(' ') <4:
				keyphrases = extractor.get_n_best(n=2)
			elif comment.count(' ') <10:
				keyphrases = extractor.get_n_best(n=3)
			else:
				keyphrases = extractor.get_n_best(n=5)

			for key in keyphrases:
				print(key[0])
				file.write(key[0]+",")
			file.write('\n')
		
		except Exception as e: 
			# print(e)
			pass



		# print(keyphrases)