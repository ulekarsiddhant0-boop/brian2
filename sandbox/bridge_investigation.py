from brian2 import *

# 1. Define a simple model (The "Architecture")
# This represents the 'recipe' Marcel mentioned.
tau = 10*ms
eqs = '''
dv/dt = -v/tau : 1
'''
G = NeuronGroup(10, eqs, threshold='v>1', reset='v=0', method='exact')
G.v = 'rand()'

# 2. Extract the "State" (The "Ingredients")
# This is what store/restore currently handles.
current_state = G.get_states()

print("--- ARCHITECTURE RECONNAISSANCE ---")
print(f"Equations defined: \n{G.equations}")
print(f"Model variables: {list(G.variables.keys())}")

print("\n--- STATE SNAPSHOT ---")
print(f"Captured variables: {list(current_state.keys())}")
# Displaying a sample of the actual numerical data
print(f"Sample 'v' values: {current_state['v']}")

# 3. THE GAP (The Goal of your GSoC Project)
print("\n--- THE GAP ANALYSIS ---")
print("Currently, 'current_state' contains the numbers, but not the 'eqs' string.")
print("Goal: Create a unified 'BrianArchive' that binds the equations to the data.")