#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[44]:


class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, lr=1, epochs=100):
        self.W = np.zeros(input_size+1)
        # add one for bias
        self.epochs = epochs
        self.lr = lr
    
    def activation_fn(self, x):
        #return (x >= 0).astype(np.float32)
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a
    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(x)
                e = d[i] - y
                print(x, y, e)
                self.W = self.W + self.lr * e * x


# In[54]:


Y = np.array([
        [0],[2],[4],[6],[8],[10],
        [1],[3],[5],[7],[9],[11]
    ])

array = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

X = [[x for y in range(1)] for x in range(1000)]

d = np.arange(0, 1000, 1)
for i in range(len(d)):
    if i % 2 == 0:
        d[i] = 0;
    else:
        d[i] = 1;


# In[55]:


perceptron = Perceptron(input_size=1)
perceptron.fit(X, d)
print(perceptron.W)


# In[ ]:




