import re

#questions and responses
question = {
    r"(hi|hello|hey)": ["Hello!", "Hi!", "Hey, how can I help you?",],
    r"how are you": ["Thankyou for asking. I'm fine, how are you?", "Thankyou for asking. I'm Great, how are you?" ],
    r"what's your name": ["I'm Ano.", "You can call me Ano."],
    r"bye|goodbye": ["Goodbye! Have a great day!", "Bye! Feel free to return if you have more questions."],


}

# Chatbot function
def chatbot_response(user_input):
    for pattern, responses in question.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return responses
    return []

# Main loop
print("Ano: Hi! I'm Ano. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Ano: Goodbye! Have a great day!")
        break
    
    responses = chatbot_response(user_input)
    if responses:
        print("ChatBot:", responses[0])
    else:
        print("ChatBot: I'm sorry, I don't understand that.")
