---
layout: default
title: Data Structure
nav_order: 7
---
# Main Data Structure
These are the data structure highlighted in the [SCRUF-D FAcct Paper](content/papers/2021_FAccT_SCRUF.pdf), along with possible ways to implementing each structure in OBP.

### User Recommendation List (l)
Machine learning algorithm (e. g. IPWLearner)
  - Context: User Profile (omega) 
  - Output: Actions: itemIDs (v) and Positions: 0... N-1

### Allocation History(H)
Bandit feedback collection of agent allocations with time index

### Choice History(L)
  - Bandit feedback collection of user recommendation list (l) with time index
  - Bandit feedback collection of agent recommendation lists (l_f) with time index
  - Bandit feedback collection of choice function output list (l_c) with time index

### Fairness metric for agent (m_i)
Off-Policy Estimator (OPE)
   - Context: Allocation History (H)
  - Context: Choice History(L)
  - Output: rating within [0,1]

### Compatibility metric for agent (c_i)
Off-Policy Estimator (OPE)
  - Context: User Profile (omega)
  - Output: rating within [0,1]

### Fairness Agent Recommendation Function (R)
Machine learning algorithm (e. g. IPWLearner) or hardcoded algorithm
  - Context: User Profile (omega)
  - Context: ItemID (v)
  - Output: rating

### Allocation Mechanism
Machine learning algorithm(s) (e. g. IPWLearner)
  - Context: Fairness metric evaluations (m_F)
  - Context: Compatibility metric evaluations(c_F)
  - Actions: Fairness Agents (f)
  - Output: Agent allocation (beta) as action_distribution
