# Employee Performance Analysis
# Generated for: 24f2009283@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# Load employee dataset
df = pd.read_csv("employee_data.csv")

# Frequency count for HR department
hr_count = (df["department"] == "HR").sum()
print("Number of employees in HR department:", hr_count)

# Create histogram (bar chart) for department distribution
plt.figure(figsize=(8, 5))
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Frequency")
plt.tight_layout()

# Save visualization
plt.savefig("department_distribution.png")
plt.show()
