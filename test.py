from graphviz import Digraph
import pandas as pd

# nfa = {'A': {'a': ['A', 'B'], 'b': ['A']}, 'B': {'a': [], 'b': ['C']}, 'C': {'a': ['C'], 'b': ['C']}}

# nfa = {'P': {'0': ['P', 'Q'], '1': ['P']}, 'Q': {'0': ['R'], '1': ['R']}, 'R': {'0': ['S'], '1': []}, 'S': {'0': ['S'], '1': ['S']}}
nfa = {'P': {'0': ['Q', 'S'], '1': ['Q']}, 'Q': {'0': ['R'], '1': ['Q', 'R']}, 'R': {'0': ['S'], '1': ['P']}, 'S': {'0': [], '1': ['P']}}

final_states = ['Q','S'] 
paths = list(nfa[list(nfa.keys())[0]].keys())
new_states = ["".join(list(nfa.keys()))]
keys = new_states[:]
dfa = {}
dfa[new_states[0]] = {}

# while len(new_states) != 0:
#     state = new_states[0]
#     dfa[state] = {}
#     for path in paths:
#         temp = []
#         for char in state:
#             temp += nfa[char][path]
#         temp = list(set(temp))
#         temp.sort()
#         temp = "".join(temp)
#         dfa[state][path] = temp
#         if temp not in keys:
#             new_states.append(temp)
#             keys.append(temp)
#     new_states.remove(state)

# print all the possible states with the while loop please
while len(new_states) != 0:
    state = new_states[0]
    print(new_states)
    dfa[state] = {}
    for path in paths:
        temp = []
        for char in state:
            temp += nfa[char][path]
        temp = list(set(temp))
        temp.sort()
        temp = "".join(temp)
        dfa[state][path] = temp
        print(dfa)
        if temp not in keys:
            new_states.append(temp)
            keys.append(temp)
    new_states.remove(state)

print("\nDFA :- \n")    
print(dfa)

df = pd.DataFrame(dfa)
df = df.transpose()
print(df)

def visualize_nfa(nfa, final_states):
    dot = Digraph(comment='NFA')
    dot.attr(rankdir='LR')
    
    for state, transitions in nfa.items():
        if state in final_states:
            dot.node(state, peripheries='2')
        else:
            dot.node(state)
        for symbol, to_states in transitions.items():
            for to_state in to_states:
                dot.edge(state, to_state, label=symbol)
    
    return dot

def visualize_dfa(dfa, final_states):
    dfa_dot = Digraph(comment='DFA')
    dfa_dot.attr(rankdir='LR')
     
    for new_state, transitions in dfa.items():
        is_final = False
        for state in final_states:
            if state in new_state:
                is_final = True
                break
        if is_final:
            dfa_dot.node(new_state, peripheries='2')
        else:
            dfa_dot.node(new_state)
        for symbol, to_state in transitions.items():
            dfa_dot.edge(new_state, to_state, label=symbol)
             
    return dfa_dot


nfa_df = pd.DataFrame(nfa)
nfa_df = nfa_df.transpose()
print(nfa_df)

dot = visualize_nfa(nfa, final_states)
dot.render('nfa', view=True)

dfa_dot = visualize_dfa(dfa, final_states)
dfa_dot.render('dfa', view=True)