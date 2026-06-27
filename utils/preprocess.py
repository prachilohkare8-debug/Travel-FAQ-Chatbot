import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

# Initialize tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess(text):
    """
    Preprocess text using NLP techniques.

    Steps:
    1. Convert to lowercase
    2. Tokenize
    3. Remove punctuation
    4. Remove stopwords
    5. Lemmatize
    6. Return cleaned sentence
    """

    # Convert to lowercase
    text = text.lower()

    # Tokenize
    tokens = word_tokenize(text)

    cleaned_words = []

    for token in tokens:

        # Remove punctuation
        if token in string.punctuation:
            continue

        # Keep only alphabetic words
        if not token.isalpha():
            continue

        # Remove stopwords
        if token in stop_words:
            continue

        # Lemmatize
        token = lemmatizer.lemmatize(token)

        cleaned_words.append(token)

    return " ".join(cleaned_words)