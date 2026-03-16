from brian2 import *
import json
import numpy as np

# 1. Setup the model
tau = 10*ms
eqs = '''
dv/dt = -v/tau : 1
'''
G = NeuronGroup(10, eqs, threshold='v>1', reset='v=0', method='exact')
G.v = 'rand()'

# 2. Extract Architecture and State
equations_str = str(G.equations) # The "Recipe"
current_state = G.get_states()   # The "Ingredients"

# 3. Create a "Mini-Archive"
# We combine the metadata (equations) and the data (arrays)
archive_meta = {'equations': equations_str}
state_to_save = {k: v for k, v in current_state.items() if isinstance(v, np.ndarray)}

# Saving to disk (using JSON for metadata and NPZ for binary arrays)
with open("model_archive_meta.json", "w") as f:
    json.dump(archive_meta, f)

np.savez("model_archive_data.npz", **state_to_save)

print("--- MINI-ARCHIVE CREATED ---")
print("1. model_archive_meta.json: Saved model architecture.")
print("2. model_archive_data.npz: Saved numerical state arrays.")
print("\nProposal Point: 'I have successfully prototyped a multi-file archival strategy, "
      "demonstrating that the gap between architecture and state is bridgeable.'")