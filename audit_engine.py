import pandas as pd

print("===== NEXCORE OPERATIONS AUDIT ENGINE =====\n")

# Load dataset
try:
    df = pd.read_csv("sample_tasks.csv")
except FileNotFoundError:
    print("Error: sample_tasks.csv not found.")
    exit()

total_hours = df["Hours_Per_Week"].sum()
founder_hours = df[df["Owner"] == "Founder"]["Hours_Per_Week"].sum()

founder_dependency_score = (founder_hours / total_hours) * 100

# Workload distribution
workload = df.groupby("Owner")["Hours_Per_Week"].sum().sort_values(ascending=False)

# Role imbalance index (highest load vs average)
average_load = workload.mean()
max_load = workload.max()
role_imbalance_index = round((max_load / average_load), 2)

# Operational Health Score
health_score = 100 - founder_dependency_score

# Risk classification
if founder_dependency_score > 60:
    risk_level = "High Risk"
elif founder_dependency_score > 40:
    risk_level = "Moderate Risk"
else:
    risk_level = "Low Risk"

# Delegation Priority Ranking
founder_tasks = df[df["Owner"] == "Founder"].sort_values(
    by="Hours_Per_Week", ascending=False
)

print(f"Total Weekly Operational Hours: {total_hours}")
print(f"Founder Weekly Hours: {founder_hours}")
print(f"Founder Dependency Score: {round(founder_dependency_score,2)}%")
print(f"Operational Health Score: {round(health_score,2)}/100")
print(f"Risk Level: {risk_level}")
print(f"Role Imbalance Index: {role_imbalance_index}\n")

print("Workload Distribution:")
print(workload, "\n")

print("Delegation Priority (High to Low Impact):")
for _, row in founder_tasks.iterrows():
    print(f"- {row['Task']} ({row['Hours_Per_Week']} hrs/week)")

print("\n===== STRATEGIC RECOMMENDATIONS =====")

if risk_level == "High Risk":
    print("• Immediate delegation required.")
    print("• Restructure ownership matrix.")
elif risk_level == "Moderate Risk":
    print("• Gradual delegation recommended.")
    print("• Introduce structured reporting rhythm.")
else:
    print("• Maintain current structure.")