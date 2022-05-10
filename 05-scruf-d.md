---
layout: default
title: SCRUF-D Integration
nav_order: 5
---

**Similarities**
- Both reference logged data: Both use feedback logs to improve predictions 
- Both use similar data structures: UserID, Lists

**Differences**
- OBP uses reward system
- OBP is based on Machine Learning driven by data and SCRUFF-D is more model based
- Metrics (OPB is rewards based)

**Implementation**
*Partial*
1. OBP as recommender system
2. Build Algorithm and Choice Mechanism, feedback separately

*Full*
1. Modifications (Similar to Slate)
  a. Evaluators/ Metrics
  b. Bandit Feedback
  c. Determine data sources/storage
2. Rewards Problem
  a. Set all rewards equal to 1
  b. Repurpose the rewards label: Could signal protected items/lists
3. Fairness Agents
  a. Each Fariness Agent serves as an OBP policy
  b. Allocation Mechanism manages policy usage based on BanditFeedback: Nested actions
4. List Structure
  a. OBP uses three dimension (context,actions,posion): SCRUFF-D uses (userID, ItemID, pposition)
  b. Context,ListID could be used in OBP, but we would need to pull list from data source
