# 🎓 ScholarMatch: Student Similarity & Performance Analyzer

## 🚀 Overview

This project analyzes student performance and finds students most similar to the topper using **cosine similarity**.

It simulates a basic **recommendation system** that can be used by coaching institutes to:

* Identify students similar to toppers
* Group students by performance patterns
* Track consistency and trends

---

## 🧠 Features

* Calculate total marks
* Identify topper
* Compute cosine similarity with topper
* Rank students by similarity
* Export results to CSV

---

## 🛠 Tech Stack

* Python
* NumPy
* Pandas

---

## 📊 How it works

Each student is treated as a **vector of marks**:
[Maths, Science, English]

Similarity is calculated using:

Cosine Similarity = (A · B) / (|A| × |B|)

---

## ▶️ Run the project

```bash
pip install -r requirements.txt
python main.py
```

---

## 📁 Output

* `student_similarity.csv` → contains similarity scores

---

## 💡 Future Improvements

* Add visualization (graphs)
* Build web interface
* Support more subjects
* Cluster students automatically

---

## 👩‍💻 Author

Aastha Shanker
