```python
import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.preprocess import preprocess


class TravelFAQChatbot:

    def __init__(self):

        # Load FAQ JSON
        BASE_DIR = Path(__file__).resolve().parent.parent
        FAQ_FILE = BASE_DIR / "faq.json"

        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

        # Prepare corpus
        self.corpus = []

        for faq in self.faqs:
            text = faq["question"] + " " + " ".join(faq["keywords"])
            self.corpus.append(preprocess(text))

        # TF-IDF Vectorizer
        self.vectorizer = TfidfVectorizer()

        self.faq_vectors = self.vectorizer.fit_transform(self.corpus)

    def get_response(self, user_question):

        cleaned_question = preprocess(user_question)

        user_vector = self.vectorizer.transform([cleaned_question])

        similarity_scores = cosine_similarity(
            user_vector,
            self.faq_vectors
        )

        best_index = similarity_scores.argmax()

        best_score = similarity_scores[0][best_index]

        # Similarity Threshold
        if best_score < 0.35:

            return {
                "reply": """Sorry, I couldn't find a suitable answer.

Please ask travel-related questions such as:

✈️ Flight Booking
🏨 Hotel Booking
🛄 Baggage
📄 Passport & Visa
🎫 Ticket Cancellation
💳 Payments
🌍 Holiday Packages""",

                "matched_question": "No Match",

                "similarity": round(best_score * 100, 2)
            }

        matched = self.faqs[best_index]

        return {

            "reply": matched["answer"],

            "matched_question": matched["question"],

            "similarity": round(best_score * 100, 2)

        }


chatbot = TravelFAQChatbot()

