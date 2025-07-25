
# 🎯 Spam SMS Detection using Logistic Regression, Naive Bayes, SVM, and TF-IDF

This repository contains a machine learning web app that detects whether an SMS message is **Spam** or **Ham** using **TF-IDF vectorization** and multiple classifiers: **Logistic Regression**, **Naive Bayes**, and **SVM**. The app is deployed with **Gradio** on Hugging Face Spaces.

---

## 🚀 Live Demo  
You can try the app instantly on Hugging Face Spaces:  
👉 https://huggingface.co/spaces/Trashika112/Spam_SMS_Detection

---

## 📌 Project Description

Spam message classification is a popular and practical NLP task, useful for filtering malicious or unwanted SMS content. This project includes:

✅ **TF-IDF Vectorization**: Converts text into numerical features based on word importance  
✅ **Multiple Classifiers**: Choose between Logistic Regression, Naive Bayes, or SVM  
✅ **Gradio Web Interface**: Easy-to-use browser-based UI for testing predictions  
✅ **Binary Classification**: Classifies messages as spam (`1`) or ham (`0`)

---

## 🛠️ Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/trashika112/spam-sms-detection.git
cd spam-sms-detection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

---

## 📁 Project Files

- `app.py` – Gradio app script for SMS classification  
- `logistic_model.pkl` – Trained Logistic Regression model  
- `naive_bayes_model.pkl` – Trained Naive Bayes model  
- `svm_model.pkl` – Trained Support Vector Machine model  
- `tfidf_vectorizer.pkl` – Fitted TF-IDF vectorizer  
- `requirements.txt` – Python dependency list  

---

## 📦 Dependencies

```txt
gradio
scikit-learn==1.6.1
pandas
joblib
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📊 Dataset

The model was trained on the [SMS Spam Collection Dataset] from Kaggle, which contains 5,000+ real SMS messages labeled as "spam" or "ham".

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to contribute:

1. Fork the repository  
2. Create a new feature branch  
3. Commit your changes  
4. Push to your branch  
5. Open a pull request

---

## 🔮 Future Work

🔁 Add ensemble or deep learning models (e.g., BERT)  
📲 Package into a mobile-friendly app  
📉 Show model confidence/probabilities in predictions  
📂 Add spam keyword heatmaps or explanations

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Trashika S Karkera**  

