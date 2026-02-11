from sklearn.feature_extraction.text import CountVectorizer

texts = ["free money now","money transfer today"]

a = CountVectorizer()
X = a.fit_transform(texts)

print(X.toarray())
