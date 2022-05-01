#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


xor = pd.DataFrame([[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]])
x = xor.iloc[:, :2]
y = xor.iloc[:, -1]


# In[3]:


from keras.layers import Layer
from keras import backend as K

class RBFLayer(Layer):
    def __init__(self, units, gamma, **kwargs):
        super(RBFLayer, self).__init__(**kwargs)
        self.units = units
        self.gamma = K.cast_to_floatx(gamma)

    def build(self, input_shape):
        self.mu = self.add_weight(name='mu',
                                  shape=(int(input_shape[1]), self.units),
                                  initializer='uniform',
                                  trainable=True)
        super(RBFLayer, self).build(input_shape)

    def call(self, inputs):
        diff = K.expand_dims(inputs) - self.mu
        l2 = K.sum(K.pow(diff, 2), axis=1)
        res = K.exp(-1 * self.gamma * l2)
        return res

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.units)


# In[4]:


from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.losses import binary_crossentropy, mse

model = Sequential()
model.add(Flatten(input_shape=(2, 1)))
model.add(RBFLayer(50, 0.5))
model.add(Dense(1, activation='tanh'))

model.compile(optimizer='sgd', loss=mse)


# In[5]:


model.fit(x, y, epochs=500)


# In[6]:


model.predict([[0, 0]])


# In[ ]:





# In[ ]:




