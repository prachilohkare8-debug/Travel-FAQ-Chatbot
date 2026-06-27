from utils.chatbot import get_answer

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = get_answer(question)

    print("Bot:", answer)