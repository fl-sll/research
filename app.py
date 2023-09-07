from flask import render_template, request, jsonify
import random
from flask import Flask

app = Flask(__name__)

import random
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

with open('data.json', 'r') as json_data:
    intents = json.load(json_data)

X = []
y = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        X.append(pattern)
        y.append(intent['tag'])


vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

labels = list(set(y))
label_to_idx = {label: idx for idx, label in enumerate(labels)}
y_numeric = np.array([label_to_idx[label] for label in y])


param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf', 'sigmoid'],
    'gamma': ['scale', 'auto'] + [0.001, 0.01, 0.1, 1, 10]
}


svm_model = SVC()
grid_search = GridSearchCV(svm_model, param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_tfidf, y_numeric)
best_svm_model = grid_search.best_estimator_


def classify_intent(user_input):
    user_input_tfidf = vectorizer.transform([user_input])
    predicted_label_numeric = best_svm_model.predict(user_input_tfidf)
    predicted_label = labels[predicted_label_numeric[0]]
    return predicted_label

def chatbot_loop(user_input, intent):
    bot_name = "Faculty"
    
    user_input_tfidf = vectorizer.transform([user_input])
    similarity_scores = user_input_tfidf.dot(X_tfidf.T).toarray()[0]
    max_similarity = np.max(similarity_scores)

    if max_similarity < 0.5:
        return f"{bot_name}: I do not understand..."

    for intent_data in intents['intents']:
        if intent_data['tag'] == intent:
            responses = intent_data['responses']
            response = f"{bot_name}: " + random.choice(responses)
            return response
    
    return f"{bot_name}: I do not understand..."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    intent = classify_intent(user_input)
    response = chatbot_loop(user_input, intent)
    return jsonify({'bot_response': response})

if __name__ == '__main__':
    app.run(debug=True)