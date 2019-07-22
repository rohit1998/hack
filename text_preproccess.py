import nltk
from nltk.corpus import stopwords
import string
import re
import pdb
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

with open("comments") as f:
	t = f.read()

t = re.sub(r'http\S+', '', t)
tokens = [nltk.word_tokenize(item) for item in t.split('\n\n\n\n')]

# pdb.set_trace()
# print(tokens)

stop_words = stopwords.words('english')
stop_words.append('I')

cleantext = []

with open("comments2",'w') as file:
	for comment in tokens:
		for word in comment:
			word = re.sub('[^A-Za-z0-9]+', '', word)
			if (word not in stop_words and word!='' and word!='\n'):
				# print(word)
				word = lemmatizer.lemmatize(word)
				cleantext.append(word)
				file.write(word+" ")
		cleantext.append('\n')
		file.write('\n')
	# print(cleantext)

