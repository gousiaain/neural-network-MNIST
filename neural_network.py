import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

# Load the MNIST dataset (70,000 handwritten digit images)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalise pixel values from 0-255 to 0-1
x_train, x_test = x_train / 255.0, x_test / 255.0

print("Training images:", x_train.shape)
print("Test images:", x_test.shape)
# Build the neural network
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Input layer: 784 neurons
    keras.layers.Dense(128, activation='relu'),   # Hidden layer: 128 neurons
    keras.layers.Dense(10, activation='softmax')  # Output layer: 10 neurons (digits 0-9)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()
# Train the model
print("Training...")
model.fit(x_train, y_train, epochs=5)

# Test the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"\nTest accuracy: {test_acc * 100:.2f}%")
# Visualise predictions
predictions = model.predict(x_test)

plt.figure(figsize=(10,5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(x_test[i], cmap='gray')
    predicted = np.argmax(predictions[i])
    actual = y_test[i]
    plt.title(f"P:{predicted} A:{actual}")
    plt.axis('off')
plt.show()