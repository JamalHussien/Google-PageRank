# Google-PageRank
## Overview
This program calculates the PageRank of a set of web pages using the iterative method. The PageRank algorithm assigns a numerical ranking to each web page based on the structure of hyperlinks, reflecting the importance of the page. The program also includes a simple search engine functionality, allowing users to query a term and get a list of pages sorted by their PageRank.

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

- The damping factor (\( \epsilon \)) ensures that the random surfer has a small probability of jumping to any page, preventing the system from getting stuck in dead ends or spider traps.
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

