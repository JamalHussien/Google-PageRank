# Google-PageRank
## Overview
This program calculates the PageRank of a set of web pages using the iterative method. The PageRank algorithm assigns a numerical ranking to each web page based on the structure of hyperlinks, reflecting the importance of the page. The program also includes a simple search engine functionality, allowing users to query a term and get a list of pages sorted by their PageRank.

## Table of Contents
1. [Concepts](#concepts)
   - [Transition Matrix (Stochastic Matrix)](#transition-matrix-stochastic-matrix)
   - [Teleportation and Damping Factor](#teleportation-and-damping-factor)
   - [Markov Process and Steady-State Distribution](#markov-process-and-steady-state-distribution)
   - [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Functions and Key Sections](#functions-and-key-sections)
   - [getPageRank](#getpagerank)
   - [Data Preparation](#data-preparation)
   - [Transition Matrix](#transition-matrix)
   - [PageRank Calculation](#pagerank-calculation)
   - [Visualization](#visualization)
   - [Search Functionality](#search-functionality)
5. [Notes](#notes)
6. [Conclusion](#conclusion)

## Concepts

### Transition Matrix (Stochastic Matrix)

- The transition matrix \( T \) represents the probabilities of moving from one page to another. Each element \( T_{ij} \) in the matrix represents the probability of moving from page \( i \) to page \( j \).
- The transition probabilities are normalized, so the sum of probabilities for each row equals 1.

### Teleportation and Damping Factor

- The damping factor (\( epsilon \)) ensures that the random surfer has a small probability of jumping to any page, preventing the system from getting stuck in dead ends or spider traps.
- The teleportation matrix \( E \) represents uniform transition probabilities to any page, and the blended matrix \( L \) combines \( T \) and \( E \).

### Markov Process and Steady-State Distribution

- The PageRank algorithm models the web as a Markov process. The dominant eigenvector of the transition matrix \( G \) represents the steady-state distribution, corresponding to the PageRank values.

### Eigenvalues and Eigenvectors

- The largest eigenvalue of the stochastic matrix \( G \) is always 1, and the corresponding eigenvector (dominant eigenvector) represents the steady-state distribution or the PageRank vector.

## Requirements
- Python 3.x
- `matplotlib` for plotting
- `numpy` for numerical operations
- `pickle` for loading the graph data
- `networkx` for handling graph structures

## Usage
1. ensure the dataset and required files (e.g., HTML files and DG.pkl) are available in the working directory.
2. Run the script to calculate PageRank and visualize the rank evolution over iterations.
3. Use the search functionality to query for specific terms and retrieve the ranked list of pages.

## Functions and Key Sections
### getPageRank
``` python
def getPageRank(fname):
    return R[0, f2i[fname]]
```
- Purpose: Retrieve the PageRank score for a given file name.
- Parameters: fname - The name of the file (web page).
- Returns: The PageRank score of the specified file.

### Data Preparation
``` python
links = {}
fnames = ['angelinajolie.html', 'bradpitt.html', 'jenniferaniston.html', 'jonvoight.html', 'martinscorcese.html', 'robertdeniro.html']
for file in fnames:
  links[file] = []
  f = open(file)
  for line in f.readlines():
      while True:
          p = line.partition('<a href="http://')[2]
          if p == '':
              break
          url, _, line = p.partition('\">')
          links[file].append(url)
  f.close()
```
- Purpose: Extract hyperlinks from each HTML file and store them in the links dictionary.
- Structure: links[file] contains a list of URLs linked from the file.

### Transition Matrix
``` python
DG = pickle.load(open('DG.pkl', 'rb'))
NX = len(fnames)
T = np.matrix(np.zeros((NX, NX)))
f2i = dict((fn, i) for i, fn in enumerate(fnames))
# Populate the transition matrix T
for predecessor, successors in DG.adj.items():
    for s, edata in successors.items():
        T[f2i[predecessor], f2i[s]] = edata['weight']
```
- Purpose: Load a directed graph DG and construct the transition matrix T.
- Explanation: f2i maps filenames to indices, and T is populated with transition probabilities between pages based on the links.

### PageRank Calculation
``` python
epsilon = .01
E = np.ones(T.shape) / NX
L = T + E * epsilon
G = np.matrix(np.zeros(L.shape))
G = L / L.sum(axis=1)
PI = np.random.random(NX)
PI /= PI.sum()
R = PI.copy()
for _ in range(100):
    R = np.dot(R, G)
```
- Purpose: Calculate the PageRank vector R using an iterative method.
- Explanation: epsilon adds a small value to ensure every page can be reached from any other page, making G a stochastic matrix. The initial rank vector PI is normalized, and the iteration updates R to converge to the final PageRank values.

### Visualization
``` python
evolution = [np.dot(PI, np.linalg.matrix_power(G, i)) for i in range(1, 20)]
plt.figure()
for i in range(G.shape[1]):
    plt.plot([step[0, i] for step in evolution], label=fnames[i], lw=2)
plt.title('rank vs iterations')
plt.xlabel('iterations')
plt.ylabel('rank')
plt.legend()
plt.show()
```
- Purpose: Visualize the evolution of PageRank scores over iterations.
- Explanation: Plots the rank of each page across the first 19 iterations, showing how the PageRank values converge.
#### plot
![plot](https://github.com/user-attachments/assets/900ad14c-1e52-4457-a02e-08ddce007082)

### Search Functionality
``` python
revind = {}
for fname in fnames:
    for line in open(fname).readlines():
        for token in line.split():
            if token in revind:
                if fname in revind[token]:
                    revind[token][fname] += 1
                else:
                    revind[token][fname] = 1
            else:
                revind[token] = {fname: 1}
result = revind['film'].keys()
sorted(result, key=getPageRank, reverse=True)
```
- Purpose: Implement a basic search functionality to find pages containing a specific keyword (e.g., 'film') and sort them by PageRank.
- Explanation: revind is a reverse index mapping words to the pages they appear in. The pages containing the queried term are sorted based on their PageRank scores.

### Notes
Ensure all required files and dependencies are correctly set up before running the script.

### Conclusion
This documentation provides an overview and detailed explanation of the Google PageRank program. The code calculates the PageRank of a set of web pages, visualizes the convergence process, and includes a simple search functionality. Use this documentation as a guide to understand and extend the implementation for your purposes.

