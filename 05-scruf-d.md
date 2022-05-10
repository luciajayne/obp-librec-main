---
layout: default
title: SCRUF-D Integration
nav_order: 5
---

# SCRUF-D Integration

### Similarities
- Both reference logged data: Both use feedback logs to improve predictions 
- Both use similar data structures: UserID, Lists

### Differences
- OBP uses reward system
- OBP is based on Machine Learning driven by data and SCRUFF-D is more model based
- Metrics (OPB is rewards based)

### Possible Implementation
All the following are various ways of integrating OBP into the SCRUF-D architecture.
*(not currently implemented, but are possible solutions)*

#### Partial
1. OBP as recommender system
2. Build Algorithm and Choice Mechanism, feedback separately

#### Full
- Modifications (Similar to [Slate](https://github.com/st-tech/zr-obp/blob/master/obp/dataset/synthetic_slate.py))
  1. Evaluators/ Metrics
  2. Bandit Feedback
  3. Determine data sources/storage
- Ways to manage the **Rewards Problem**
  1. Set all rewards equal to 1
  2. Repurpose the rewards label: Could signal protected items/lists
- Ways to manage the **Fairness Agents**
  1. Each Fariness Agent serves as an OBP policy
  2. Allocation Mechanism manages policy usage based on BanditFeedback: Nested actions
- Ways to manage the **List Structure**
  1. OBP uses three dimension (context,actions,posion): SCRUFF-D uses (userID, ItemID, pposition)
  2. Context,ListID could be used in OBP, but we would need to pull list from data source
