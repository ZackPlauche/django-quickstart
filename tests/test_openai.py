from jurni.openai import Message, generate_message

messages = [
    Message('assistant', 'What is your favorite color?'),
    Message('user', 'Purple'),
]

message = generate_message(messages)
print(message)