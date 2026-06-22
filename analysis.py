import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("student_cleaned.csv")

# Show data
print(df.head())

# 1. Average marks
average_marks = {
    "Math": df["Math"].mean(),
    "Science": df["Science"].mean(),
    "English": df["English"].mean()
}

plt.figure(figsize=(7,5))
plt.bar(
    average_marks.keys(),
    average_marks.values(),
    color=["blue","green","orange"]
)

plt.title("Average Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.savefig("average_marks.png")
plt.show()


# 2. Grade distribution

df["Grade"].value_counts().plot(
    kind="bar",
    color="purple"
)

plt.title("Student Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")

plt.savefig("grade_distribution.png")
plt.show()


print("Charts created successfully!")