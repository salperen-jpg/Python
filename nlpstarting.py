from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize


#Getting out stop words.
example='Please sit your own place , and try to not disturb anybody. Thanks for your attention'
stop_words=set(stopwords.words('english'))

words=word_tokenize(example)

filtered=[w for w in words if w not in stop_words]


print(stop_words)
print(filtered)

