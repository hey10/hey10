#!/usr/bin/env python
# coding: utf-8

# In[12]:


#developing a function that can make predictions

def predict(row, weights):  #function predicts an o/p value for a row given a set of weights
    activation = weights[0] #bias

    for i in range(len(row) - 1):  #for each row not considering first input
        activation += weights[i + 1] * row[i] #summing product of weights and corresponding inputs
                                              #i+1 because first element of weight is bias
                                              #initializing activation with bias as bias is added
    return 1.0 if activation >= 0.0 else 0.0 #threshold condition


# In[13]:


#sample dataset for testing predict function

dataset = [
    [2.7810836,2.550537003,0],
    [1.465489372,2.362125076,0],
    [3.396561688,4.400293529,0],
    [1.38807019,1.850220317,0],
    [3.06407232,3.005305973,0],
    [7.627531214,2.759262235,1],
    [5.332441248,2.088626775,1],
    [6.922596716,1.77106367,1],
    [8.675418651,-0.242068655,1],
    [7.673756466,3.508563011,1]
]

weights = [-0.1, 0.20653640140000007, -0.23418117710000003] #randomly initialized weights


# In[14]:


#Prediction over dataset

for row in dataset:
    prediction = predict(row, weights)
    print("Expected = ",row[-1], "Predicted = ",prediction)


# In[15]:


#estimating weight values for dataset
#the following function trains the perceptron and adjusts it's weight on each iteration

def train_weights(train, learning_rate, n_epoch):
    weights = [0.0 for i in range(len(train[0]))] #initialize weights by simply assigning 0
                                                  #l(t[0]): is based on length of first row
    #loop over each epoch
    for epoch in range(n_epoch): #for training multiple times we use nepochs
        sum_error = 0.0  #to capture error
        
        #loop over each row in the data for an epoch
        for row in train: #updation of each row
            prediction = predict(row, weights)
            error = row[-1] - prediction #loss function
            sum_error += error**2  #introducing error on weight updation, modify error
            weights[0] += learning_rate * error #updating bias
            
            #loop over each weight and update it for a row in an epoch
            for i in range(len(row)-1): #for each row not considering first input
                weights[i+1] += learning_rate * error * row[i]#weight updation if error occurs
                
        print(epoch, learning_rate, sum_error)
    return weights


# In[16]:


#calculating weights

learning_rate = 0.1   #amount of weight updation
n_epoch = 5           #number of iterations through data while updating weights

weights = train_weights(dataset, learning_rate, n_epoch)
weights


# In[17]:


#Perceptron for AND Gate dataset

AND_dataset = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
]


# In[18]:


#Training over AND dataset

AND_weights = train_weights(AND_dataset, learning_rate, n_epoch)
AND_weights


# In[19]:


#Prediction over AND dataset

for row in AND_dataset:
    prediction = predict(row, weights)
    print("Expected = ",row[-1], "Predicted = ",prediction)


# In[20]:


#Perceptron for OR Gate dataset

OR_dataset = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1],
]


# In[21]:


#Training over OR dataset

OR_weights = train_weights(OR_dataset, learning_rate, n_epoch)
OR_weights


# In[22]:


#Prediction over OR dataset

for row in OR_dataset:
    prediction = predict(row, weights)
    print("Expected = ",row[-1], "Predicted = ",prediction) 

