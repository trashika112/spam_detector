
import streamlit as st
import joblib

# Load vectorizer and models
vectorizer = joblib.load("tfidf_vectorizer.pkl")
models = {
    "Logistic Regression": joblib.load("logistic_model.pkl"),
    "Naive Bayes": joblib.load("naive_bayes_model.pkl"),
    "SVM": joblib.load("svm_model.pkl")
}

st.title("📧 Spam Detection App")
st.write("Choose a model and enter a message to check if it's spam or ham.")

model_choice = st.selectbox("Select Model", list(models.keys()))
message = st.text_area("Enter your message", "")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        model = models[model_choice]
        X_input = vectorizer.transform([message])
        prediction = model.predict(X_input)[0]
        label = "🟢 Ham" if prediction == 0 else "🔴 Spam"
        st.success(f"Prediction ({model_choice}): {label}")
