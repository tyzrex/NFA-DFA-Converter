import itertools
import pandas as pd
from graphviz import Digraph

def get_nfa_from_user():
    num_states = int(input("Enter the number of states in the NFA: "))
    states = input("Enter the states separated by space: ").split()
    num_symbols = int(input("Enter the number of symbols in the NFA: "))
    symbols = input("Enter the symbols separated by space: ").split()
    start_state = input("\nEnter the start state in the NFA: ")
    final_states = input("Enter the final states separated by space: ").split()
    nfa = {}
    
    for i in range(num_states):
        state = input("\nEnter the state: ")
        nfa[state] = {}
        
        for j in range(num_symbols):
            path = input("\nEnter the path: ")
            print("Enter end state from state {} traveling through path {}: ".format(state, path))
            reaching_state = input().split()
            nfa[state][path] = reaching_state
            
    print("NFA: ", nfa)
    print("NFA in tabular format: ")
    df = pd.DataFrame(nfa)
    df = df.transpose()
    print(df)
    
    return nfa, final_states, symbols

def get_subsets_list(nfa):
    states = set(nfa.keys())
    subsets = []
    for r in range(len(states) + 1):
        subsets.extend(list(itertools.combinations(states, r)))
    return [list(subset) for subset in subsets]

def get_transition_table(nfa,symbols):
    subsets = get_subsets_list(nfa)
    subsets.sort()
    transition_table = []
    for subset in subsets:
        row = []
        for symbol in symbols:
            next_states = set()
            for state in subset:
                next_states.update(nfa.get(state, {}).get(symbol, []))
            next_states = sorted(list(next_states))
            next_states = [''.join(sorted(s)) for s in next_states]
            next_states.sort()
            row.append(next_states)
        transition_table.append([''.join(sorted(subset)), row[0], row[1]])
    df = pd.DataFrame(transition_table, columns=['State', symbols[0], symbols[1]])
    return df

def nfa_to_dfa(nfa):
    # Initialize the dfa dictionary and a list to store new states
    paths = list(nfa[list(nfa.keys())[0]].keys())
    new_states = [list(nfa.keys())[0]]

    keys = list(nfa.keys())
    dfa = {}
    dfa[new_states[0]] = {}

    while len(new_states) != 0:
        state = new_states[0]
        dfa[state] = {}
        for path in paths:
            temp = []
            for char in state:
                temp += nfa[char][path]
            temp = list(set(temp))
            temp.sort()
            temp = "".join(temp)
            dfa[state][path] = temp
            if temp not in keys:
                new_states.append(temp)
                keys.append(temp)
        new_states.remove(state)
    
    return dfa
    

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

def main():
    nfa, final_states, symbols = get_nfa_from_user()
    # nfa = {'P': {'0': ['P', 'Q'], '1': ['P']}, 'Q': {'0': ['R'], '1': ['R']}, 'R': {'0': ['S'], '1': []}, 'S': {'0': ['S'], '1': ['S']}}
    # final_states = ['S']
    # symbols = ['0', '1']
    
    print("\n\nNFA: ")
    print(nfa)
    
    transition_table = get_transition_table(nfa,symbols)
    print("\n\nTransition table: ")
    print(transition_table)
    
    nfa_dot = visualize_nfa(nfa, final_states)
    nfa_dot.render('NFA', view=True)
    
    dfa = nfa_to_dfa(nfa)
    dfa_dot = visualize_dfa(dfa, final_states)
    dfa_dot.render('DFA', view=True)
    
if __name__ == '__main__':
    main()