
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\lab\Downloads\archive (2) (1).zip")

# Clean column names (removes spaces issues)
df.columns = df.columns.str.strip()

# Check columns
print(list(df.columns))
print(df.head())

# Use first two columns
x = df.iloc[:, 0].values
y = df.iloc[:, 1].values

# Add outlier
x = np.append(x, 0.2)
y = np.append(y, 2)

# Plot
plt.boxplot([x, y], labels=['X values', 'Y values'])
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.title("Boxplot of X and Y (with Outlier)")
plt.show()
['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

import pandas as pd
import matplotlib.pyplot as plt

# --- Load dataset ---
df = pd.read_csv(r"C:\Users\lab\Downloads\archive (2) (1).zip")  # update filename if needed

# --- Check columns ---
print("Columns in dataset:", df.columns)

# --- Use correct columns ---
x = df["total_bill"]
y = df["tip"]

# --- Plot ---
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label="Data")

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Total Bill vs Tip Scatter Plot")

plt.legend()
plt.grid(True)

plt.show()
Columns in dataset: Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='object')

 
