#!/usr/bin/env bash

pip install -r requirements.txt

python -m nltk.downloader punkt
python -m nltk.downloader punkt_tab
python -m nltk.downloader stopwords
python -m nltk.downloader wordnet
python -m nltk.downloader omw-1.4