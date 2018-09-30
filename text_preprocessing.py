from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from string import digits, punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

def text_processing(string):
    remove_digits = str.maketrans('', '', digits)
    remove_punctuations = str.maketrans("", "", punctuation)
    cach_stopwords = set([text.translate(remove_punctuations) for text in stopwords.words('english')])
    lemmatizer = WordNetLemmatizer()
    stemmer = LancasterStemmer()
    # convert to lower case
    lower_string = string.lower()
    # remove all the punctuations
    no_punc_string = lower_string.translate(remove_punctuations)
    # remove all digits
    no_digit_string = no_punc_string.translate(remove_digits)
    # split the string
    splited_string = no_digit_string.split()
    # remove stop words
    splited_string_stop = [word for word in splited_string if word not in cach_stopwords]
    # call lemmatizer
    lemmatized_words = [lemmatizer.lemmatize(word) for word in splited_string_stop]
    # call stemmer
    stemmed_words = [stemmer.stem(word) for word in lemmatized_words]
    return ( " ".join(stemmed_words))

def data_processing(df):
    df_new=df[df.stars.isin([1,5])]
    text=df_new.text
    y=df_new.stars
    text.index=df_new.shape[0]
    sample_reviews=[]
    for i in range(0, text.size):
        sample_reviews.append(text_processing(text[i]))
    return(sample_reviews)

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2))
X=tfidf_vectorizer.fit_transform(sample_reviews)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
score_log = logreg.score(X_test, y_test)
print(score_log)

svm = LinearSVC(C=1)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
score_svm = svm.score(X_test, y_test)
print(score_svm)