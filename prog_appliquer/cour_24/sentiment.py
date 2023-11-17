from nltk.classify import MaxentClassifier
import nltk
nltk.download('pros_cons')
from nltk.corpus import pros_cons
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import mark_negation, extract_unigram_feats
from nltk.tokenize import word_tokenize

pros_docs = cons_docs = []
n_exemples = 500
for i in range(n_exemples):
    pros_docs.append((pros_cons.sents(categories='Cons')[i], 'Cons'))
    cons_docs.append((pros_cons.sents(categories='Pros')[i], 'Pros'))
    print("+++ ",pros_cons.sents(categories='Pros')[i])
    print("--- ",pros_cons.sents(categories='Cons')[i])

train_pros_docs = pros_docs[:int(0.8*n_exemples)]
test_pros_docs = pros_docs[int(0.8*n_exemples):n_exemples]
train_cons_docs = cons_docs[:int(0.8*n_exemples)]
test_cons_docs = cons_docs[int(0.8*n_exemples):n_exemples]
training_docs = train_pros_docs+train_cons_docs
testing_docs = test_pros_docs+test_cons_docs

sentim_analyseur = SentimentAnalyzer()
tous_mots_neg = sentim_analyseur.all_words([mark_negation(doc) for doc in training_docs])
unigrammes = sentim_analyseur.unigram_word_feats(tous_mots_neg, min_freq=4)

sentim_analyseur.add_feat_extractor(extract_unigram_feats, unigrams=unigrammes)
training_set = sentim_analyseur.apply_features(training_docs)

test_set = sentim_analyseur.apply_features(testing_docs)
sentim_analyseur.train(MaxentClassifier.train, training_set)

for cle,valeur in sorted(sentim_analyseur.evaluate(test_set).items()):
	print('{0}: {1}'.format(cle, valeur))
	
phrases_difficiles = [
	"Most tools are shit.",
	"This tool is the shit.",
	"These systems has never been good.",
	"I won't say that the product is astounding and I wouldn't claim that \
	it is too banal either.",
	"I like to hate this company, but I couldn't fault this one",
	"It's one thing to try it, but another thing entirely \
	to pay for it",
	"This product was too good",
	"This was actually neither that useful, nor super duper."
]

for ph in phrases_difficiles:
    jetons = word_tokenize(ph)
    print(jetons, end = " ")
    print(sentim_analyseur.classify(jetons))

while True:
    print('Votre critique: ', end='')
    critique = input()
    if not len(critique):
        break
    jetons = word_tokenize(critique)
    print(jetons, end = " ")
    print(sentim_analyseur.classify(jetons))
    

