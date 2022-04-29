#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re

regex_if = "if\s*\([^\{\}]*\)"
regex_while = "while\s*\([^\{\}]*\)"
regex_for = "for\s*\([^\{\}]*\)"


# In[4]:


with open("if_statement_code.java",'r') as src_files:
    src_prg=''.join(src_files.readlines())
    if re.search(regex_if, src_prg):
        print("Has a valid java if statement")
    else:
        print("Has an invalid java if statement")


# In[7]:


with open("while_loop_code.java",'r') as src_files:
    src_prg=''.join(src_files.readlines())
    if re.search(regex_while, src_prg):
        print("Has a valid java if statement")
    else:
        print("Has an invalid java if statement")


# In[8]:


with open("for_loop_code.java",'r') as src_files:
    src_prg=''.join(src_files.readlines())
    if re.search(regex_for, src_prg):
        print("Has a valid java if statement")
    else:
        print("Has an invalid java if statement")


# In[ ]:




