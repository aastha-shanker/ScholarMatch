import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

df["total"] = df["Marks_Math"] + df["Marks_Science"] + df["Marks_English"]
topper_index = df["total"].idxmax()
topper = df.loc[topper_index]

print("Topper name:", topper["Name"])
print("Score:", topper["total"])


features = ["Marks_Math", "Marks_Science", "Marks_English"]
topper_vector = topper[features].values


def similarity(a, b):
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)

    if mag_a == 0 or mag_b == 0:
        return 0

    return (a @ b) / (mag_a * mag_b)

similarity_list = []

for i in range(len(df)):
    current_vector = df.loc[i, features].values
    sim = similarity(topper_vector, current_vector)
    similarity_list.append(sim)

df["similarity"] = similarity_list

df_sorted = df.sort_values(by="similarity", ascending=False)
df_sorted.to_csv("student_similarity.csv", index=False)
print("Analysis completed")
print("File saved as student_similarity.csv")