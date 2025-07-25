import gradio as gr
import joblib

# Load vectorizer and models
vectorizer = joblib.load("tfidf_vectorizer.pkl")
log_model = joblib.load("logistic_model.pkl")
nb_model = joblib.load("naive_bayes_model.pkl")
svm_model = joblib.load("svm_model.pkl")

# Prediction function
def predict_spam(message, model_name):
    if not message.strip():
        return "⚠️ Please enter a message."
    
    X_input = vectorizer.transform([message])
    
    model = {
        "Logistic Regression": log_model,
        "Naive Bayes": nb_model,
        "SVM": svm_model
    }[model_name]
    
    prediction = model.predict(X_input)[0]
    
    return "🟢 Ham" if prediction == 0 else "🔴 Spam"

# Create Gradio Interface
app = gr.Interface(
    fn=predict_spam,
    inputs=[
        gr.Textbox(label="Enter your message"),
        gr.Radio(["Logistic Regression", "Naive Bayes", "SVM"], label="Choose a Model")
    ],
    outputs="text",
    title="📧 Spam Message Detector",
    description="Classify text messages as spam or ham using ML models"
)

# Run the app
if __name__ == "__main__":
    app.launch()
