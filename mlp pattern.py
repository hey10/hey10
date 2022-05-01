#!/usr/bin/env python
# coding: utf-8

# In[9]:


from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

iris = load_iris()
x = iris.data
y = iris.target
df = pd.DataFrame(data=np.c_[x, y], columns = iris['feature_names'] + ['target'])
df.head()

from math import exp
from random import seed
from random import random
def init_network(n_inputs, n_hidden, n_outputs):
    network         = list()
    #List of dictionary access by weight id , each dicttionary representing a hidden layer
                        # intializing weights for a H-Layer                 # for n no of H-Layers
    hidden_layer    = [{'weights': [random() for i in range(n_inputs + 1)]} for j in range(n_hidden)]
    network.append(hidden_layer)

    #similar logic as above
    output_layer    = [{'weights':[random() for i in range(n_hidden + 1)]} for j in range(n_outputs)]
    network.append(output_layer)

    return network

def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation
"""
def softmax(weights, inputs):
    activation = weights[-1]
    for 
"""

def transfer(activation):
    #sigmoid
	return 1.0 / (1.0 + exp(-activation))

def forward_propogate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        
        for layer_no in range(len(layer)):
            activation         = activate(layer[layer_no]['weights'], inputs)
            layer[layer_no]['output']    = transfer(activation)
            new_inputs.append(layer[layer_no]['output'])
        inputs = new_inputs

    return inputs

def transfer_derivative(output):
	return output * (1.0 - output)

def backward_propagate(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()

		if i != len(network)-1:# for hidden layers
			for j in range(len(layer)): #for neurons in hidden layer
				error = 0.0
				for neuron in network[i + 1]:# for each next layer neuron connected to the current neuron of each hidden layer
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)

		else:#output layer
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(neuron['output'] - expected[j])

		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] -= l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] -= l_rate * neuron['delta']

def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propogate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[int(row[-1])] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate(network, expected)
			update_weights(network, row, l_rate)
		print('Epoch : %d, Learining rate : %.3f, Error : %.3f' % (epoch, l_rate, sum_error))
	return sum_error

# splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

train_df = pd.DataFrame(data=np.c_[X_train, y_train])
test_df = pd.DataFrame(data=np.c_[X_test, y_test])

#training data
dflist = train_df.values.tolist()
print(dflist[0])
network = init_network(4, 2, 3)
print(network)
error = train_network(network, dflist, 0.01, 10000, 3)

#testing function
dftest_list = test_df.values.tolist()

toterror = 0
for row in dftest_list:
    pred = forward_propogate(network, row)
    maxele = max(pred)
    idx = pred.index(maxele)
    #print(idx)
    if idx != row[-1]:
        toterror += 1
print(f'Total incorrect classifications : {toterror} Accuracy : {(len(dftest_list)-toterror)/len(dftest_list) * 100}%')


# In[ ]:





# In[12]:


from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

iris = load_iris()
x = iris.data
y = iris.target
df = pd.DataFrame(data=np.c_[x, y], columns = iris['feature_names'] + ['target'])
df.head()

from math import exp
from random import seed
from random import random
def init_network(n_inputs, n_hidden, n_outputs):
    network         = list()
    #List of dictionary access by weight id , each dicttionary representing a hidden layer
                        # intializing weights for a H-Layer                 # for n no of H-Layers
    hidden_layer    = [{'weights': [random() for i in range(n_inputs + 1)]} for j in range(n_hidden)]
    network.append(hidden_layer)

    #similar logic as above
    output_layer    = [{'weights':[random() for i in range(n_hidden + 1)]} for j in range(n_outputs)]
    network.append(output_layer)

    return network

def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
"""
def softmax(weights, inputs):
    activation = weights[-1]
    for 
"""

def transfer(activation):
    #sigmoid
	return 1.0 / (1.0 + exp(-activation))

def forward_propogate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        
        for layer_no in range(len(layer)):
            activation         = activate(layer[layer_no]['weights'], inputs)
            layer[layer_no]['output']    = transfer(activation)
            new_inputs.append(layer[layer_no]['output'])
        inputs = new_inputs

    return inputs

def transfer_derivative(output):
	return output * (1.0 - output)

def backward_propagate(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()

		if i != len(network)-1:# for hidden layers
			for j in range(len(layer)): #for neurons in hidden layer
				error = 0.0
				for neuron in network[i + 1]:# for each next layer neuron connected to the current neuron of each hidden layer
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)

		else:#output layer
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(neuron['output'] - expected[j])

		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] -= l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] -= l_rate * neuron['delta']

def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propogate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[int(row[-1])] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate(network, expected)
			update_weights(network, row, l_rate)
		print('Epoch : %d, Learining rate : %.3f, Error : %.3f' % (epoch, l_rate, sum_error))
	return sum_error

# splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

train_df = pd.DataFrame(data=np.c_[X_train, y_train])
test_df = pd.DataFrame(data=np.c_[X_test, y_test])

#training data
dflist = train_df.values.tolist()
print(dflist[0])
network = init_network(4, 2, 3)
print(network)
error = train_network(network, dflist, 0.01, 10000, 3)

#testing function
dftest_list = test_df.values.tolist()

toterror = 0
for row in dftest_list:
    pred = forward_propogate(network, row)
    maxele = max(pred)
    idx = pred.index(maxele)
    #print(idx)
    if idx != row[-1]:
        toterror += 1
print(f'Total incorrect classifications : {toterror} Accuracy : {(len(dftest_list)-toterror)/len(dftest_list) * 100}%')


# In[ ]:




