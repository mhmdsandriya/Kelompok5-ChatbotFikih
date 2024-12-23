import json
import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open('data/intents.json', 'r') as file:
    intents = json.load(file)

# Prepare data
corpus = []
labels = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        labels.append(intent['tag'])

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
y = labels

# Model training
model = LogisticRegression()
model.fit(X, y)

# Chatbot function
def chatbot_response(user_input):
    input_vector = vectorizer.transform([user_input])
    tag = model.predict(input_vector)[0]
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

# Main loop
if __name__ == "__main__":
    print("Fiqih is ready to chat about waste management! Type 'quit' to exit.")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'quit':
            break
        response = chatbot_response(user_input)
        print("Bot:", response)
