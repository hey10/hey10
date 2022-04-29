#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import json

opr_priority = {'=': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

inp_str = "op = a + b / c + d * f"
operands = re.findall("[a-zA-Z][a-zA-Z]*", inp_str)
operators = re.findall("[\+\-\*/=\^]", inp_str)

temp_ctr, temp, quadra = 0, 't', []

while operators:
    opr = max(operators, key = lambda x: opr_priority[x])
    ind = operators.index(opr)
    op1, op2 = operands[ind], operands[ind + 1]
    operators.remove(opr)
    del operands[ind: ind + 2]
    res = temp + str(temp_ctr)
    if opr == "=":
        res, op1, op2 = op1, op2, '-'
    operands.insert(ind, res)
    quadra.append([res, opr, op1, op2])
    temp_ctr += 1

print("\nInput: \n", inp_str)
print("\nRes\tOper\tOp1\tOp2")
for row in quadra:
    for elem in row:
        print(elem, end = "\t")
    print()

print()
print("Target Code: \n")
table = json.load(open("table.json"))
for row in quadra:
    opr = row[1]
    for instruction in table[opr]:
        print(instruction)

print()








# In[ ]:




