import pandas as pd

# Load dataset
df = pd.read_csv("student_raw.csv")

print("Original Dataset")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Gender
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Clean names
df["Name"] = df["Name"].str.strip().str.title()

# Fix gender values
df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "male": "Male",
    "female": "Female"
})

# Fix wrong marks
df.loc[df["Math"] > 100, "Math"] = 100
df.loc[df["Math"] < 0, "Math"] = 0

# Remove wrong age
df = df[df["Age"] <= 100]

# Save cleaned data
df.to_csv("student_cleaned.csv", index=False)

print("\nCleaning Completed!")
print(df)