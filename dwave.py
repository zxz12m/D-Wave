import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Define the MaxCut problem as a binary constraint satisfaction problem (CSP)
csp = dwavebinarycsp.factories.max_cut(G1_py)

# Convert the CSP to a binary quadratic model (BQM) in Ising format
bqm = dwavebinarycsp.stitch(csp)

# Define the D-Wave sampler and embedding composite to submit the problem to the quantum annealer
sampler = EmbeddingComposite(DWaveSampler(solver={'topology__type': 'chimera'}))

# Submit the problem to the quantum annealer and retrieve the best solution
response = sampler.sample(bqm, num_reads=1000)
solution = response.first.sample

# Print the best solution and its corresponding energy
print("Best solution:", solution)
print("Energy of best solution:", response.first.energy)
