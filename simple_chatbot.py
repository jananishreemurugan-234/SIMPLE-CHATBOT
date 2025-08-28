# simple_chatbot.py

# Dictionary of predefined responses
responses = {
    "hello": "Hi there! Welcome to Tamizhan Skills.",
    "hi": "Hello! How can I assist you?",
    "courses": "We offer Python, Data Science, AI, and more.",
    "fees": "Please visit our website or contact support for fee details.",
    "contact": "You can reach us at contact@tamizhanskills.com.",
    "bye": "Goodbye! Have a great day!"
}

def chatbot_response(user_input):
    user_input = user_input.lower()   # Convert to lowercase for matching
    return responses.get(user_input, "I'm sorry, I don't understand that. Can you rephrase?")

print("Tamizhan Skills Chatbot (type 'bye' to exit)")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_message)
    print("Bot:", response)