import re

symb_tab = []
addr = 100

with open(r"D:\Jayesh\Msc CS\Sem 2\Compiler Design and Construction\Prac 7 - Symbol Table Creation\var_declarations.txt", 'r') as src_file:
  for line in src_file.readlines():
    dtype, defined = '-', 0
    tokens = re.findall('[a-zA-Z][a-zA-Z0-9]*', line)
    for token in tokens:
      if token in ['int', 'float', 'string', 'char']:
        dtype = token
        tokens.remove(token)
        defined = 1
        break
    variables = tokens
    for var in variables:
      if var in [row[0] for row in symb_tab]:
        continue
      symb_tab.append([var, dtype, addr, defined])
      addr += 1

# for row in symb_tab:
#   print(row)
    
print('\nName\tDT\tMemLoc\tDefined')
for row in symb_tab:
 for elem in row:
   print(elem, end = '\t')
 print()

print()
