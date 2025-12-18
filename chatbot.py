def greet_user():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot.")
    print("🤖 Chatbot: You can type 'bye' anytime to exit.\n")


def load_whatsapp_messages(filename):
    messages = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if " - " in line:
                    parts = line.split(" - ", 1)
                    message = parts[1]

                    if ": " in message:
                        message = message.split(": ", 1)[1]

                    messages.append(message.strip().lower())
    except FileNotFoundError:
        print("⚠️ WhatsApp chat file not found!")

    return messages

whatsapp_messages = load_whatsapp_messages("WhatsApp Chat with CSE-02 OFFICIAL")


def get_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! Nice to meet you.",
        "how are you": "I'm just a program, but I'm doing great! 😊",
        "what is your name": "I'm a simple Python chatbot.",
        "help": "I can chat with you! Try saying hello or asking how I am.",
        "joke": "Why do programmers love Python? Because it has great libraries! 😂",
        "bye": "Goodbye! Have a great day! 👋"
    }

    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

    for msg in whatsapp_messages:
        if user_input in msg or msg in user_input:
            return f"This reminds me of a WhatsApp message: \"{msg}\""

    return "Sorry, I didn't understand that. Can you rephrase?"


def chatbot():
    greet_user()

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("🤖 Chatbot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    chatbot()
