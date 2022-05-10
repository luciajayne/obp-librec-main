---
layout: default
title: OBP vs. SCRUF-D
nav_order: 4
---

**OBP OVERVIEW** 
The focus is on offline experimentation 
[OBP Tutorial](https://sites.google.com/cornell.edu/recsys2021tutorial) 

**OBP PROCESS**
![OBP Process](https://raw.githubusercontent.com/st-tech/zr-obp/master/images/overview.png) 

**Data Management** 
i. Datasets 
ii. Bandit Feedback 
  1. Dictionary storing logged data 
  2. Action_context: Context vectors characterizing actions (i.e., a vector representation or an embedding of each action). 
  3. OBP Extension (Slate) 
    a. Comparison of bandit feedback 
**Off-Policy Learner** <br />
[OBP Off-Policy Learner Notebook] (https://colab.research.google.com/github/st-tech/zr-obp/blob/master/examples/quickstart/opl.ipynb) 
i. Class wrapper for ML model 
  1. Example IPWLearner  
  2. Off-policy learner based on Inverse Probability Weighting and Supervised Classification. 
ii. Outputs  
  1. predictions  
  2. action_probabilty distributions(where len_size = 1) 
c. Simulation 
  i. Based on online policy mainly 
d. Off-Policy Estimators (OPE) 
  i. Policy values (metrics) based on reward system 
  ii. Return values within [0,1] 
  iii. Estimates the performance of a policy based on log history 
