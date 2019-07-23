from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'C:\Users\rohgupt\Downloads\stanford-corenlp-full-2018-10-05')

sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
print ('Tokenize:', nlp.word_tokenize(sentence))
print ('Part of Speech:', nlp.pos_tag(sentence))
print ('Named Entities:', nlp.ner(sentence))
print ('Constituency Parsing:', nlp.parse(sentence))
print ('Dependency Parsing:', nlp.dependency_parse(sentence))
nlp.close() # Do not forget to close! The backend server will consume a lot memery.