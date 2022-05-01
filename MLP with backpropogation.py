#!/usr/bin/env python
# coding: utf-8

# In[28]:


def initialize_network(n_inputs, n_hidden, n_outputs): # Initialize a network
    network = list()
    
    #for each of the hidden layers we've to specify range
    #this part sets the weight value for single neuron wrt all i/ps
    hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)] #1= bias
    network.append(hidden_layer)
    
    #this is for all the neurons in hidden layers
    output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)] #every out is connected to hidden
    network.append(output_layer)
    return network


#random weights are assigned for the hidden layers

seed(1)# init the no (generate a no 2 it wont go )
network = initialize_network(2, 1, 2) #as many as hidden/op layers that much will b bias
for layer in network:  #for each layer in network print the layer
    print(layer)


# In[29]:


#multilayer perceptron is created now we'll compute o/p for each of the neurons


def activate(weights, inputs): #adder function 
    activation = weights[-1] #bias
    for i in range(len(weights)-1): #for each row not considering 1st input
        activation += weights[i] * inputs[i] #summing up
    return activation


# In[30]:


def transfer(activation): #sigmoid activation function
    return 1.0 / (1.0 + exp(-activation))


# In[31]:


def forward_propagate(network, row): #forward propogate to go from 1st layer to last layer
    inputs = row
    for layer in network: #we've to go for each layer & each neuron
        new_inputs = []
        for neuron in layer: #like layer by layer  we have to move forward
            activation = activate(neuron['weights'], inputs)# activate in neuron then transfer to activation 
            #function then qwe ll gwt o/p , o/t will be input for next layer
            neuron['output'] = transfer(activation) #storing o/p in o/p column of each neuron
            
            #now the o/p of hidden layer will be i/p for o/p layer
            new_inputs.append(neuron['output'])
        inputs = new_inputs #output 
    return inputs


# In[40]:


# test forward propagation
network = [[{'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],[{'weights': [0.2550690257394217, 0.49543508709194095]}, {'weights': [0.4494910647887381, 0.651592972722763]}]]
row = [1, 0, None]
output = forward_propagate(network, row)
print(output)


# In[33]:


def transfer_derivative(output):
    return output * (1.0 - output)
#slope of the curve to find max and min value


# In[34]:


# now to differnce btw actual op and desired op which is error so for that this function
def transfer_derivative(output):
    return output * (1.0 - output)

def backward_propagate_error(network, expected): #bp to go from o/p layer to prev hidden layer
    for i in reversed(range(len(network))):
        
        #so basically we have to  update each layer 
        layer = network[i]
        
        #errors needs to be calculated for each neuron so list is created
        errors = list()
        
        #2 cases to calculate error: i)for o/p layer ii)for hidden layer
        
        #EXPECT O/P LAYER
        if i != len(network)-1:  #-1 bec will exclude the o/p layer and i = per layer
            for j in range(len(layer)):# weight for every neuron is 0 
                error = 0.0
                
                #i+1 = next layer of neuron
                for neuron in network[i + 1]:  #error = (weight_k * error_j) 
                    #* transfer_derivative(output) #next layer is connected to prev
                    
                    # + sign bec error will not only be calculated bt also added
                    error += (neuron['weights'][j] * neuron['delta']) 
                    #error = (output - expected) * transfer_derivative(output)
                errors.append(error)
        else:
            for j in range(len(layer)):  #O/P 
                neuron = layer[j]
                errors.append(neuron['output'] - expected[j]) 
        for k in range(len(layer)):
            neuron = layer[k]
            neuron['delta'] = errors[k] * transfer_derivative(neuron['output'])
            
# test backpropagation of error
network = [[{'output': 0.7105668883115941, 'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],[{'output': 0.6213859615555266, 'weights': [0.2550690257394217, 0.49543508709194095]}, {'output': 0.6573693455986976, 'weights': [0.4494910647887381, 0.651592972722763]}]]
expected = [0, 1]
backward_propagate_error(network, expected)
for layer in network:
    print(layer)


# In[35]:


# Update network weights with error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        
        #last column of row consists of o/p class 
        inputs = row[:-1]
        
        #if network is not in 1st(hidden) layer
        if i != 0:# except the first layer ,o/p layer= input for next
            inputs = [neuron['output'] for neuron in network[i - 1]]# last column
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] -= l_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] -= l_rate * neuron['delta']


# In[36]:


from random import seed
from random import random
 
# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch): # no of iteration
        sum_error = 0 # to capture error
        for row in train: 
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, l_rate)
        print('epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
        
        


# In[37]:


# Test training backprop algorithm
seed(1)
dataset = [[2.7810836,2.550537003,0],
    [1.465489372,2.362125076,0],
    [3.396561688,4.400293529,0],
    [1.38807019,1.850220317,0],
    [3.06407232,3.005305973,0],
    [7.627531214,2.759262235,1],
    [5.332441248,2.088626775,1],
    [6.922596716,1.77106367,1],
    [8.675418651,-0.242068655,1],
    [7.673756466,3.508563011,1]]
n_inputs = len(dataset[0]) - 1   # last column
n_outputs = len(set([row[-1] for row in dataset])) #last column o/p 
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.9, 20, n_outputs)
for layer in network:
    print(layer)


# In[38]:


def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))


# In[39]:


from math import exp
 
# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation
 
# Transfer neuron activation
def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))
 
# Forward propagate input to a network output
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs
 
# Make a prediction with a network
def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))
 
    
# Test making predictions with the network
dataset = [[2.7810836,2.550537003,0],
    [1.465489372,2.362125076,0],
    [3.396561688,4.400293529,0],
    [1.38807019,1.850220317,0],
    [3.06407232,3.005305973,0],
    [7.627531214,2.759262235,1],
    [5.332441248,2.088626775,1],
    [6.922596716,1.77106367,1],
    [8.675418651,-0.242068655,1],
    [7.673756466,3.508563011,1]]
network = [[{'weights': [-1.482313569067226, 1.8308790073202204, 1.078381922048799]}, {'weights': [0.23244990332399884, 0.3621998343835864, 0.40289821191094327]}],
    [{'weights': [2.5001872433501404, 0.7887233511355132, -1.1026649757805829]}, {'weights': [-2.429350576245497, 0.8357651039198697, 1.0699217181280656]}]]
for row in dataset:
    prediction = predict(network, row)
    print('Expected=%d, predicted=%d' % (row[-1], prediction))


# In[ ]:





# In[ ]:




