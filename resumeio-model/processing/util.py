import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
punctuation = "'''–“”’!()-•[]{};:'\"\,<>/?@#$%^&*_~+'''"


def parse_text(text):
    text_word_list = []
    text = ' '.join(word for word in text.split() if not any(c.isdigit() for c in word))
    for word in text:
        if word in punctuation:
            text = text.replace(word, "")
        if word == '.':
            text = text.replace(word, "\n")
    sentence_list = text.split("\n")
    for sentence in sentence_list:
        split_sentence = sentence.split()
        split_sentence = list(filter(lambda word: word.lower() not in stop_words, split_sentence))
        tokens = nltk.word_tokenize(' '.join(split_sentence))
        tags = nltk.pos_tag(tokens)
        words = [word for word, pos in tags
                 if (pos == 'NN' or pos == 'NNP' or pos == 'VBZ')]
        words = list(map(lambda word: lemmatizer.lemmatize(word.lower()), words))
        text_word_list.append(words)
    return text_word_list


def get_most_important_words(text):
    text = parse_text(text)
    word_dictionary = {}
    for sentence in text:
        for word in sentence:
            if word not in word_dictionary.keys():
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1
    return [word for word in word_dictionary]
