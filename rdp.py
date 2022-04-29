
prod_rules = """
S -> aCd
C -> p | q
"""

def is_valid(inp_str):
    i = 0
    def adv():
        nonlocal i 
        i += 1
    def S():
        if inp_str[i] == 'a':
            adv()
            if C():
                adv()
                if inp_str[i] == "d" and len(inp_str) - 1 == i:
                    return True
        return False
    def C():
        if inp_str[i] == 'p' or inp_str[i] == 'q':
            return True
        return False
    return S()

print("\nGrammar:", prod_rules)
inp = input("Enter string: \n")
if is_valid(inp):
    print("{} is a valid string".format(inp))
else:
    print("{} is an invalid string".format(inp))

print()





# """
# T → FT'
# T' → *FT' | ε
# F → (T') | i
# """

# def is_it_valid(inp_str):
#     i = 0
#     def adv():
#         nonlocal i 
#         i += 1
#     def T():
#         if F():
#             adv()
#             if T_prime() and len(inp_str) - 1 == i:
#                 return True
#         return False
#     def T_prime():
#         nonlocal i
#         if i < len(inp_str) and inp_str[i] == "*":
#             adv()
#             if F():
#                 adv()
#                 if T_prime():
#                     return True
#             return False
#         i -= 1
#         return True
#     def F():
#         if inp_str[i] == "(":
#             adv()
#             if T_prime():
#                 adv()
#                 if inp_str[i] == ")":
#                     return True
#         elif inp_str[i] == "i":
#             return True
#         return False
#     return T()

# print(is_it_valid("(*i*i*i*i)"))
    
