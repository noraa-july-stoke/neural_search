# Import necessary libraries:
# import tensorflow as tf
import os
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import tensorflowjs as tfjs
import numpy as np
from spellcheck.typo_algo import *
from typing import List, Dict

print(dir(tfjs))

# Define the training data
i_o_map = typo_setter("arnold", 1, 1, {})
print(len(i_o_map))
# Derive separate lists from I/O mappings
def get_inputs(i_o_map: Dict) -> List:
    return list(i_o_map.keys())

def get_outputs(i_o_map: Dict) -> List:
    return list(i_o_map.values())

inputs: List = get_inputs(i_o_map)
outputs: List = get_outputs(i_o_map)

# Convert inputs to numerical features using one-hot encoding
all_words: List = sorted(list(set(' '.join(inputs).split())))
word_to_int: Dict = dict((w, i) for i, w in enumerate(all_words))
int_to_word: Dict = dict((i, w) for i, w in enumerate(all_words))

# the encoded inputs will be a list of lists
encoded_inputs = []
for input_string in inputs:
    encoded_input = [0] * len(all_words)
    for word in input_string.split():
        encoded_input[word_to_int[word]] = 1
    encoded_inputs.append(encoded_input)

# Convert outputs to numerical targets using label encoding
all_outputs = sorted(list(set(outputs)))
output_to_int: Dict = dict((w, i) for i, w in enumerate(all_outputs))
int_to_output: Dict = dict((i, w) for i, w in enumerate(all_outputs))

encoded_outputs: List = []
for output_string in outputs:
    encoded_outputs.append(output_to_int[output_string])


# Define the neural network model
model = Sequential()
model.add(Dense(64, input_dim=len(all_words), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(all_outputs), activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# Train the model
model.fit(np.array(encoded_inputs), np.array(encoded_outputs), epochs=100, batch_size=8)

# Save the model in TensorFlow.js format
print(model.summary())


# tfjs.save('model', model)
# output_dir = os.environ.get('OUTPUT_DIR')
# print(output_dir)
tfjs.converters.save_keras_model(model, os.path.join(model, "model"))
