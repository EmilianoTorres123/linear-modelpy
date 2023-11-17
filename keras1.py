from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(units=1, input_shape=[100])

])

model.summary()
w, b = model.weights
print(w)
print(b)

