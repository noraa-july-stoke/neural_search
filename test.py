# Import necessary libraries:
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np

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
    'go to the feed': '/feed',
    'ga to feed': '/feed',
    'ga ta feed': '/feed',
    'my notifications': '/notifications',
    'notifications': '/notifications',
    'messages': '/messages',
    'profile': '/profile',
    'settings': '/settings',
    'create post': '/feed/new',
    'search': '/search',
    'jane doe': '/search?q=jane+doe',
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

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(lr=0.001), metrics=['accuracy'])
# Here we are training the model to learn the patterns
# between the inputs and the outputs. the model is trained for 100 epochs
# with a batch size of 8. the model is trained on the encoded inputs
# and the encoded outputs.
model.fit(np.array(encoded_inputs), np.array(
    encoded_outputs), epochs=100, batch_size=8)

# Make a prediction
def predict_output(input_string):
    encoded_input = [0] * len(all_words)
    for word in input_string.split():
        if word in word_to_int:
            encoded_input[word_to_int[word]] = 1
    output_index = model.predict([encoded_input]).argmax()
    return int_to_output[output_index]

print(predict_output('go hame'))
