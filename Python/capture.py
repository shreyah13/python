import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV
df = pd.read_csv("capture.csv")

# Quick check
print(df.head())

# Count packets by protocol
protocol_counts = df['_ws.col.Protocol'].value_counts()

# Bar chart
plt.figure(figsize=(10,6))
sns.barplot(x=protocol_counts.index, y=protocol_counts.values, palette="viridis")
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")
plt.title("Packet Count per Protocol")
plt.show()



