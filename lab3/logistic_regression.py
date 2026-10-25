# Aim: To implement a Logistic Regression model for performing binary classification tasks.
import numpy as np

# Training data
X = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y = np.array([0, 0, 0, 1, 1, 1], dtype=float)

# Initialize weight and bias
w = 0.0
b = 0.0

# Learning rate and iterations
learning_rate = 0.01
iterations = 1000

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Gradient Descent
for i in range(iterations):

    # Calculate predictions
    z = w * X + b
    y_pred = sigmoid(z)

    # Calculate error
    error = y_pred - y

    # Calculate gradients
    dw = np.mean(error * X)
    db = np.mean(error)

    # Update weight and bias
    w = w - learning_rate * dw
    b = b - learning_rate * db

# Test data
X_test = np.array([2, 3, 4, 5, 7], dtype=float)

# Calculate probabilities
probability = sigmoid(w * X_test + b)

# Convert probabilities to classes
prediction = (probability >= 0.5).astype(int)

# Display results
print("Weight =", w)
print("Bias =", b)

print("\nPredictions:")

for i in range(len(X_test)):
    print(
        "Hours =", X_test[i],
        "Probability =", round(probability[i], 3),
        "Class =", prediction[i]
    )
