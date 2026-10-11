
print("Welcome to my Rule-Based AI Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "your name" in user_input:
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif "how are you" in user_input:
        print("Bot: I am fine, thank you!")

    elif user_input == "help":
        print("Bot: I can greet you and answer simple questions.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    elif "capital of pakistan" in user_input:
        print("Bot: The capital of Pakistan is Islamabad.")

    elif "tell me a joke" in user_input:
        print("Bot: Why did the computer go to the doctor? Because it had a virus!")

    elif "who created you" in user_input:
        print("Bot: I was created by my developer using Python.")


    else:
        print("Bot: Sorry, I don't understand that message.")
