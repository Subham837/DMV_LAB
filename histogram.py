import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.normal(100, 15, 1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('histogram_no_comments.png')