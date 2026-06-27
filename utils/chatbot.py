import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.preprocess import preprocess


class TravelFAQChatbot:

    def __init__(self):

        # Load FAQ data
        from pathlib import Path

        BASE_DIR = Path(__file__).resolve().parent.parent

        FAQ_FILE = BASE_DIR / "faq.json"

        with open(FAQ_FILE, "r", encoding="utf-8") as file:

            self.faqs = json.load(file)
            self.faqs = json.load(file)

        # Prepare corpus
        self.corpus = []

        for faq in self.faqs:

            text = faq["question"] + " " + " ".join(faq["keywords"])

            self.corpus.append(preprocess(text))

        # TF-IDF
        self.vectorizer = TfidfVectorizer()

        self.faq_vectors = self.vectorizer.fit_transform(self.corpus)

    def get_response(self, user_question):

        # Greeting Handling
        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]

        if user_question.lower().strip() in greetings:

            return {
                "reply":
                """👋 Hello! Welcome to the Travel FAQ Chatbot.

I can help you with:

✈ Flight Booking

🏨 Hotel Booking

🛄 Baggage

📄 Travel Documents

🎫 Ticket Cancellation

💳 Payments

How can I help you today?""",

                "matched_question": "Greeting",

                "similarity": 100
            }

        # NLP Preprocessing
        cleaned_question = preprocess(user_question)

        # Convert to TF-IDF
        user_vector = self.vectorizer.transform([cleaned_question])

        # Cosine Similarity
        similarity_scores = cosine_similarity(
            user_vector,
            self.faq_vectors
        )

        # Best Match
        best_index = similarity_scores.argmax()

        best_score = similarity_scores[0][best_index]

        # Threshold
        if best_score < 0.35:

            return {
                "reply":
                """Sorry, I couldn't understand your question.

Please ask questions related to:

• Flights

• Hotels

• Baggage

• Travel Documents

• Payments

• Holiday Packages""",

                "matched_question": None,

                "similarity": round(best_score * 100, 2)
            }

        matched = self.faqs[best_index]

        return {

            "reply": matched["answer"],

            "matched_question": matched["question"],

            "similarity": round(best_score * 100, 2)

        }


# Create chatbot object
chatbot = TravelFAQChatbot()