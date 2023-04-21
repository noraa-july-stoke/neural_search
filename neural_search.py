# This code is an example of a simple neural network that takes in strings
# as inputs and predicts a corresponding string output based on patterns
# learned from the training data. Here's a breakdown of the code with
# beginner-level explanations for each part:

# Import necessary libraries:
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np

# Define the training data
# here is an easy-to-read representation of the training data:
# as a python dictionary, where the keys are the inputs and the values
# are the outputs. the inputs are strings and the outputs are strings.
i_o_map = {
    'home': '/home',
    'go home': '/home',
    'hane': '/home',
    'gohome': '/home',
    'haeme': '/home',
    'hame': '/home',
    'my dsahboard': '/dashboard',
    'mt dashboard': '/dashboard',
    'my dashboard': '/dashboard',
    'go to my dashboard': '/dashboard',
    'feed': '/feed',
    'show me the feed': './feed',
    'go to feed': '/feed',
    'my notifications': '/notifications',
    'notifications': '/notifications',
    'messages': '/messages',
    'profile': '/profile',
    'settings': '/settings',
    'create post': '/feed/new',
    'search': '/search',
    'explore': '/explore',
    'liked posts': '/liked',
    'saved posts': '/saved',
    'recommended': '/recommended',
    'popular': '/popular',
    'popl4r': '/popular',
    'poplar': '/popular',
    'trending': '/trending',
    'new': '/new',
    'top': '/top',
    'rising': '/rising',
    'controversial': '/controversial',
    'hot': '/hot',
    'random': '/random',
    'categories': '/categories',
    'podcasts': '/podcasts',
    'videos': '/videos',
    'articles': '/articles',
    'news': '/news',
    'gifs': '/gifs/latest',
    'giphs': '/gifs/latest',
    'memes': '/memes',
    'books': '/books',
    'create new note': '/notes/new',
    'games': '/games'
}


def get_inputs(i_o_map):
    return list(i_o_map.keys())

def get_outputs(i_o_map):
    return list(i_o_map.values())

inputs = get_inputs(i_o_map)
outputs = get_outputs(i_o_map)

# Convert inputs to numerical features using one-hot encoding
# one-hot encoding is a way of representing categorical data as binary vectors
# it allows the representation of categorical data to be more expressive
# more info: https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/
all_words = sorted(list(set(' '.join(inputs).split())))
word_to_int = dict((w, i) for i, w in enumerate(all_words))
int_to_word = dict((i, w) for i, w in enumerate(all_words))

# the encoded inputs will be a list of lists
# that contains 1s and 0s. 1s represent the presence of a word
# in the input string, and 0s represent the absence of a word
# in the input string. In this example, the length of the encoded
# input list is the length of the all_words list.
encoded_inputs = []
for input_string in inputs:
    encoded_input = [0] * len(all_words)
    for word in input_string.split():
        encoded_input[word_to_int[word]] = 1
    encoded_inputs.append(encoded_input)

# Convert outputs to numerical targets using label encoding
# label encoding is a way of representing categorical data as integers
# it allows the representation of categorical data to be more expressive
all_outputs = sorted(list(set(outputs)))
output_to_int = dict((w, i) for i, w in enumerate(all_outputs))
int_to_output = dict((i, w) for i, w in enumerate(all_outputs))

# this time, the encoded outputs will be a list of integers
# that represent the index of the output string in the all_outputs list
# In this example, the length of the encoded output list is the length
# of the all_outputs list.
encoded_outputs = []
for output_string in outputs:
    encoded_outputs.append(output_to_int[output_string])


# Define the neural network model
# the model has 3 layers: an input layer, a hidden layer, and an output
# layer the input layer has 64 neurons and expects 1 input vector of
# the length of the all_words list
model = Sequential()
model.add(Dense(64, input_dim=len(all_words), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(all_outputs), activation='softmax'))

# Compile the model
# the loss function is sparse_categorical_crossentropy because the
# output is a single integer value. the optimizer is Adam with a learning
# rate of 0.001. the metrics are accuracy. the model is trained for 50
# epochs with a batch size of 8.
# sparse_categorical_crossentropy:
# https://keras.io/api/losses/probabilistic_losses/#sparse_categorical_crossentropy-function
# basically, sparse_categorical_crossentropy is a loss function that
# is used when the output is a single integer value. it
# calculates the loss between the predicted output and the actual output
# and then calculates the average loss over all the training examples.
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(lr=0.001), metrics=['accuracy'])


# Train the model
# basically, here we are training the model to learn the patterns
# between the inputs and the outputs. the model is trained for 50 epochs
# with a batch size of 8. the model is trained on the encoded inputs
# and the encoded outputs.
model.fit(np.array(encoded_inputs), np.array(
    encoded_outputs), epochs=50, batch_size=8)

# Make a prediction
# here is where we use the model to make a prediction. we encode the
# input string and then use the model to make a prediction. the prediction
# is a list of probabilities that the input string is each of the output
# strings. we then take the index of the highest probability and use it
# to get the output string from the all_outputs list.
# the input string is 'go hane' and the output string is '/home'
# as you can see, while "go hane":  "/home" is not key/value pair in the training data,
# explicitly, the model is able to make a prediction based on the fact that "go" and "hane"
# are found in the training data with other entries that mapped to "/home"
# One thing to note here is that the words in the input string must be
# at least present in SOME FORM in the training data. Even though they aren't
# explicitly present in that form, the model is able to make a prediction
# if yout put "happy birthday mom" as the input string, the model will
# probably not be able to make a prediction and could throw an error.
# It will more than likely be an instance of "keyerror". I bet you can guess why 🙃
# This is because building a model that can handle this is beyond the scope of
# this tutorial. If you want to learn more about how to build a model that can
# handle this, check out this channel: https://www.youtube.com/@dataschool
# You can also follow me on Medium to stay up-to-date with new tutorials!
input_string = 'happy birthday mom'
encoded_input = [0] * len(all_words)
for word in input_string.split():
    encoded_input[word_to_int[word]] = 1
prediction = model.predict(np.array([encoded_input]))
output_index = np.argmax(prediction)
output_string = int_to_output[output_index]

print('Input:', input_string)
print('Output:', output_string)
