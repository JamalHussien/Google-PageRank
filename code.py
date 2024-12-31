import matplotlib.pyplot as plt  # For plotting
import numpy as np  # For numerical computations
import pickle  # For loading serialized data
import networkx as nx  # For graph-related operations

# Function to get the PageRank of a specific file
def getPageRank(fname):
    return R[0, f2i[fname]]

# Dictionary to store links from each file
links = {}

# List of file names representing web pages
fnames = ['angelinajolie.html', 'bradpitt.html', 'jenniferaniston.html', 
          'jonvoight.html', 'martinscorcese.html', 'robertdeniro.html']

# Parse each file to extract URLs (hyperlinks)
for file in fnames:
    links[file] = []  # Initialize an empty list for the links
    f = open(file)  # Open the file
    for line in f.readlines():
        while True:
            # Extract the hyperlink from the line
            p = line.partition('<a href="http://')[2]
            if p == '':
                break  # Exit loop if no more links
            url, _, line = p.partition('\">')  # Extract URL and remaining line
            links[file].append(url)  # Add URL to the list of links
    f.close()  # Close the file

# Load the directed graph from a serialized file
DG = pickle.load(open('DG.pkl', 'rb'))

# Number of nodes/pages
NX = len(fnames)

# Initialize a transition matrix with zeros
T = np.matrix(np.zeros((NX, NX)))

# Map file names to their respective indices
f2i = dict((fn, i) for i, fn in enumerate(fnames))

# Populate the transition matrix based on the graph's adjacency data
for predecessor, successors in DG.adj.items():
    for s, edata in successors.items():
        T[f2i[predecessor], f2i[s]] = edata['weight']

# Add teleportation factor to the transition matrix
epsilon = 0.01  # Small probability for teleportation
E = np.ones(T.shape) / NX  # Uniform probability matrix
L = T + E * epsilon  # Adjusted transition matrix

# Normalize the rows of the matrix to ensure stochasticity
G = np.matrix(np.zeros(L.shape))
G = L / L.sum(axis=1)

# Initialize the PageRank vector with random values
PI = np.random.random(NX)
PI /= PI.sum()  # Normalize the vector
R = PI.copy()  # Copy the initial PageRank vector

# Iteratively compute the PageRank vector
for _ in range(100):
    R = np.dot(R, G)

# Track the evolution of ranks over iterations
evolution = [np.dot(PI, np.linalg.matrix_power(G, i)) for i in range(1, 20)]

# Plot the evolution of ranks
plt.figure()
for i in range(G.shape[1]):
    plt.plot([step[0, i] for step in evolution], label=fnames[i], lw=2)

plt.title('Rank vs Iterations')  # Title of the plot
plt.xlabel('Iterations')  # X-axis label
plt.ylabel('Rank')  # Y-axis label
plt.legend()  # Add legend to the plot
plt.show()

# Build a reverse index mapping tokens to files and their frequencies
revind = {}
for fname in fnames:
    for line in open(fname).readlines():
        for token in line.split():  # Split line into tokens
            if token in revind:
                if fname in revind[token]:
                    revind[token][fname] += 1  # Increment frequency
                else:
                    revind[token][fname] = 1  # Initialize frequency
            else:
                revind[token] = {fname: 1}  # Initialize token in the index

# Get files containing the token 'film' and sort them by PageRank
str = input('Google me!\n')
result = revind[str].keys()
print(sorted(result, key=getPageRank, reverse=True))
