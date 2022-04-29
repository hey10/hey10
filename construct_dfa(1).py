
class DFA:
    def __init__(self, start, final):
        self.trans_diag = {}
        self.start = start
        self.final = [final] if type(final) != list else final

    def add_state(self, state, transitions):
        self.trans_diag[state] = {str(key): value for key, value in transitions.items()}

    def is_valid(self, inp_str):
        curr = self.start
        for char in inp_str:
            curr = self.trans_diag[curr][char]
        if curr in self.final:
            return True
        return False


# DFA over {a, b} accepting only 2 symbols
dfa = DFA(start = 0, final = 2)
dfa.add_state(0, {'a': 1, 'b': 1})
dfa.add_state(1, {'a': 2, 'b': 2})
dfa.add_state(2, {'a': 3, 'b': 3})
dfa.add_state(3, {'a': 3, 'b': 3})
inp_str = "aa"
print("\nDFA over {a, b} accepting only 2 symbols\nInput string: ", inp_str)
if dfa.is_valid(inp_str):
    print("Accepted")
else:
    print("Rejected")


# DFA over {0, 1, 2} accepting string that starts with 0, has 1 in middle and ends with 2
dfa = DFA(start = 'q0', final = 'q3')
dfa.add_state('q0', {0: 'q1', 1: 'q4', 2: 'q4'})
dfa.add_state('q1', {0: 'q1', 1: 'q2', 2: 'q1'})
dfa.add_state('q2', {0: 'q2', 1: 'q2', 2: 'q3'})
dfa.add_state('q3', {0: 'q2', 1: 'q2', 2: 'q3'})
dfa.add_state('q4', {0: 'q4', 1: 'q4', 2: 'q4'})
inp_str = "0102021120102"
print("\nDFA over {0, 1, 2} accepting string that starts with 0, has 1 in middle and ends with 2s\nInput string: ", inp_str)
if dfa.is_valid(inp_str):
    print("Accepted")
else:
    print("Rejected")


# DFA over {a, b} accepting string starting with 'a'
dfa = DFA(start = 0, final = 1)
dfa.add_state(0, {'a': 1, 'b': 2})
dfa.add_state(1, {'a': 1, 'b': 1})
dfa.add_state(2, {'a': 2, 'b': 2})
inp_str = "abbbabaa"
print("\nDFA over {a, b} accepting string starting with 'a'\nInput string: ", inp_str)
if dfa.is_valid(inp_str):
    print("Accepted")
else:
    print("Rejected")

print()
