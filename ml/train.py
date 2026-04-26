from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 🔥 starter dataset (you can expand later)
texts = [
    "Assistant Professor recruitment",
    "Walk-in interview for JRF",
    "Project assistant position",
    "Tender for supply equipment",
    "Research fellow vacancy",
    "PhD admission open",
]

labels = [
    "Faculty",
    "Internship",
    "Internship",
    "Tender",
    "Research",
    "Research"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "ml/model.pkl")
joblib.dump(vectorizer, "ml/vectorizer.pkl")

print("✅ Model trained and saved")