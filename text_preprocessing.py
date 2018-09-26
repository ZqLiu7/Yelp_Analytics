from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from string import digits, punctuation

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



