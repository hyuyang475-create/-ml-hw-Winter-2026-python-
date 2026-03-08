import numpy as np
from sklearn.metrics import precision_score, recall_score

# Read N from user
N = int(input("Enter the number of points (N): "))

# Initialize numpy arrays for ground truth and predicted labels
X = np.zeros(N, dtype=int)
Y = np.zeros(N, dtype=int)

# Read N (x, y) points
for i in range(N):
    print(f"\nPoint {i + 1}:")
    x = int(input("  Enter x (ground truth, 0 or 1): "))
    y = int(input("  Enter y (predicted, 0 or 1): "))
    X[i] = x
    Y[i] = y

# Compute Precision and Recall using scikit-learn
precision = precision_score(X, Y, zero_division=0)
recall = recall_score(X, Y, zero_division=0)

print(f"\nPrecision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
