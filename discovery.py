from mimetypes import init
from models import DFA

def dfa_discovery(log):
    
    #dfa = DFA("Test", {1,2,3}, 1, {1,3}, {("a",1,2), ("b",2,2), ("c",1,3)})
    
    # initialise sets of final states and transitions
    final_states = set()
    transitions = set()

    # use the dictionary to enumerate the states
    state_dict = {"":0}

    state_cnt = 1
    num_of_traces = 0
    
    for trace in log:
        if num_of_traces > 100:
            break
        state = ""
        for event in trace:
           prev_state = state
           state = state + event['concept:name'] + ","
           if state not in state_dict:
               state_dict[state] = state_cnt
               state_cnt += 1
           transitions.add((event['concept:name'], state_dict[prev_state], state_dict[state]))
        final_states.add(state_dict[state])
        num_of_traces += 1
    return DFA("", set(state_dict.values()), 0, final_states, transitions)


def print_log(log):
    for trace in log:
        for event in trace:
           print(event['concept:name'])
