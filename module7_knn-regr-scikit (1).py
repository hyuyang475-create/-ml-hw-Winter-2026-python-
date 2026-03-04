import numpy as np
from sklearn.neighbors import KNeighborsRegressor

print("Welcome! This program will perform k-NN Regression based on the points you provide.")
print("-" * 60)

# --- Input: N (number of points) ---
while True:
    try:
        N = int(input("\nHow many training points do you have? (enter a positive integer): "))
        if N > 0:
            break
        else:
            print("Hmm, that doesn't seem right. Please enter a number greater than 0.")
    except ValueError:
        print("That doesn't look like a valid number. Try again!")

# --- Input: k (number of neighbors) ---
while True:
    try:
        k = int(input(f"\nGreat! And how many neighbors should k-NN consider? (k, positive integer): "))
        if k > 0:
            break
        else:
            print("k needs to be at least 1. Give it another shot!")
    except ValueError:
        print("Oops, that's not a valid number. Please try again.")

# --- Input: N (x, y) points ---
X_train = np.zeros((N, 1), dtype=float)
y_train = np.zeros(N, dtype=float)

print(f"\nPerfect! Now let's collect your {N} training point(s).")
print("For each point, you'll enter an x value and a y value — just real numbers.\n")

for i in range(N):
    print(f"  -- Point {i + 1} of {N} --")
    while True:
        try:
            x_val = float(input(f"     x = "))
            break
        except ValueError:
            print("     That's not a valid number. Please enter a real number for x.")
    while True:
        try:
            y_val = float(input(f"     y = "))
            break
        except ValueError:
            print("     That's not a valid number. Please enter a real number for y.")
    X_train[i, 0] = x_val
    y_train[i] = y_val
    print()

# --- Variance of labels ---
label_variance = np.var(y_train)
print("-" * 60)
print(f"Nice work! Here's a quick look at your training data:")
print(f"  Variance of y labels: {label_variance:.6f}")

# --- Input: query X ---
while True:
    try:
        X_query = float(input("\nNow, what x value would you like to predict y for? x = "))
        break
    except ValueError:
        print("Please enter a valid real number for x.")

# --- k-NN Regression ---
print("-" * 60)

if k <= N:
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, y_train)

    X_query_array = np.array([[X_query]])
    Y_predicted = knn_regressor.predict(X_query_array)

    print(f"\nUsing {k}-NN Regression, here's what the model predicts:")
    print(f"  For x = {X_query}")
    print(f"  Predicted y = {Y_predicted[0]:.6f}")
    print("\nHope that's helpful — good luck with your data!")
else:
    print(f"\nUh-oh! You asked for k = {k} neighbors, but you only provided {N} training point(s).")
    print(f"k can't be larger than N for k-NN to work properly.")
    print(f"Try again with k ≤ {N}, or add more training points!")
