import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("plots", exist_ok=True)

df = pd.read_csv("data.csv")

df["total"] = df["Marks_Math"] + df["Marks_Science"] + df["Marks_English"]
df["average"] = df["total"] / 3

topper_idx = df["total"].idxmax()
topper = df.loc[topper_idx]

avg_maths = df["Marks_Math"].mean()
avg_sci = df["Marks_Science"].mean()
avg_eng = df["Marks_English"].mean()

df["consistency"] = df[["Marks_Math", "Marks_Science", "Marks_English"]].std(axis=1)

def consistency_label(std):
    if std < 5:
        return "Highly Consistent"
    elif std < 15:
        return "Moderate"
    else:
        return "Inconsistent"

df["consistency_type"] = df["consistency"].apply(consistency_label)

def category(total):
    if total > 240:
        return "High Performer"
    elif total > 180:
        return "Average Performer"
    else:
        return "Needs Improvement"

df["category"] = df["total"].apply(category)

print("\n--- Insights ---")
print("Topper:", topper["Name"])

most_consistent = df.loc[df["consistency"].idxmin()]
print(f"Most consistent student: {most_consistent['Name']}")

print("Average total marks:", df["total"].mean())

def similarity(a, b):
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)
    if mag_a == 0 or mag_b == 0:
        return 0
    return np.dot(a, b) / (mag_a * mag_b)

features = ["Marks_Math", "Marks_Science", "Marks_English"]
topper_features = topper[features].values

similarity_list = []

for i in range(len(df)):
    current_vector = df.loc[i, features].values
    sim = similarity(topper_features, current_vector)
    similarity_list.append(sim)

df["similarity"] = similarity_list

df_no_topper = df[df["Name"] != topper["Name"]]

max_similar_idx = df_no_topper["similarity"].idxmax()
max_similar_student = df_no_topper.loc[max_similar_idx]

print("Most similar student:", max_similar_student["Name"])

df.to_csv("final_analysis.csv", index=False)

df_sorted = df.sort_values(by="similarity", ascending=False)
df_sorted.to_csv("student_similarity.csv", index=False)

plt.figure(figsize=(6,4))
plt.hist(df["Marks_Math"], color="pink", alpha=0.7, edgecolor="black")
plt.title("Maths Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("plots/maths_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df["Marks_Science"], color="green", alpha=0.7, edgecolor="black")
plt.title("Science Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("plots/science_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df["Marks_English"], color="blue", alpha=0.7, edgecolor="black")
plt.title("English Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("plots/english_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df["total"], df["consistency"], c=df["similarity"], cmap="coolwarm")
plt.colorbar(label="Similarity to Topper")
plt.xlabel("Total Marks")
plt.ylabel("Consistency (Std Dev)")
plt.title("Performance vs Consistency")
plt.savefig("plots/performance_vs_consistency.png", dpi=300)
plt.show()

subjects = ["Maths", "Science", "English"]
averages = [avg_maths, avg_sci, avg_eng]

plt.figure(figsize=(6,4))
plt.bar(subjects, averages, color=["blue", "green", "orange"])
plt.title("Subject Averages")
plt.ylabel("Average Marks")
plt.savefig("plots/subject_averages.png", dpi=300)
plt.show()

category_counts = df["category"].value_counts()

plt.figure(figsize=(5,5))
plt.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%")
plt.title("Student Performance Categories")
plt.savefig("plots/category_distribution.png", dpi=300)
plt.show()

print("\nAnalysis complete")
print("Plots saved in 'plots/' folder")
print("Processed dataset saved as 'final_analysis.csv'")
print("Similarity data saved as 'student_similarity.csv'")