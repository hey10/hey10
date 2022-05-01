#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install scikit-fuzzy')


# In[3]:


#yt video
import numpy as np 
import skfuzzy as fuzzy 
from skfuzzy import control as ctrl


# In[4]:


import matplotlib. pyplot as plt 
temp        = ctrl.Antecedent(np.arange(10,90,1),'temp') 
temp['lo']  = fuzzy.trimf(temp.universe, [10,10,25]) 
temp['ba']  = fuzzy.trimf(temp.universe, [15,30,45]) 
temp['av']  = fuzzy.trimf(temp.universe, [40,50,60]) 
temp['aa']  = fuzzy.trimf(temp.universe, [55,70,85]) 
temp['hi']  = fuzzy.trimf(temp.universe, [75,90,90]) 

pres        = ctrl.Antecedent(np.arange(1,5,0.05),'pres') 
pres['lo']  = fuzzy.trimf(pres.universe, [1,1,1.75]) 
pres['ba']  = fuzzy.trimf(pres.universe, [1.25,2,2.75]) 
pres['av']  = fuzzy.trimf(pres.universe, [2,3,4])
pres['aa']  = fuzzy.trimf(pres.universe, [3.25,4,4.75])
pres['hi']  = fuzzy.trimf(pres.universe, [4.25,5,5])

hp          = ctrl.Consequent(np.arange (1,5,0.05),'hp') 
hp['lo']    = fuzzy.trimf(hp.universe, [1,1,1.75]) 
hp['ba']    = fuzzy.trimf(hp.universe, [1.25,2,2.75]) 
hp['av']    = fuzzy.trimf(hp.universe, [2.5,3,3.75])
hp['aa']    = fuzzy.trimf(hp.universe, [3.5,4,4.5])
hp['hi']    = fuzzy.trimf(hp.universe, [4.25,5,5])



#temp.automf(5) 

temp.view() 
hp.view() 
pres.view() 
plt.show()


# In[5]:


rulel   = ctrl.Rule(temp['av'] & pres['av'], hp['ba'])
rule2   = ctrl.Rule(temp['hi'] & pres['hi'], hp['lo'])
#rulel   = ctrl.Rule(temp['av'] & pres['av'], hp['ba'])
tipping = ctrl.ControlSystem([rulel, rule2]) 
Tip     = ctrl.ControlSystemSimulation(tipping)  
Tip.input['temp'] = 80
Tip.input['pres'] = 4.5
Tip.compute() 
print (Tip.output['hp'])


# In[ ]:




