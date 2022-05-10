---
layout: default
title: FAQ
nav_order: 14
---
# FAQ

### What OBP expects from a recommendation perspective? 
The main purpose is to look at the log data history and create a behavior of that. It builds a model or different type of learning.

### What is the OBP algorithm section based on?
Algorithms in OBP (unsupervised learning) is machine learning where the behavior is based on the data. OBP ideally gets the data and figures out what the output should be.

### Is the OBP algorithm section the most important part of OBP?
No, because it only takes the log data and kind of creates a new behavior. OBP is more concerned about the reward because it makes recommendations of that. 

### What is IPW?
Inverse propensity weighting (IPW) means that if there is data missing, it reduces the weight of those missing items. But, it increases the data of the users that are there for future allocations. 

### What is the item_ID in IPWLearner?
The learner expands the item_ID to a vector field. Instead of having the value of the item ID, it uses ones.
 
### What is OBP input and output for this project?
The input should be user_ID and the output should be a list.

### What is the advantage of using OBP?
The advantage of OBP is to use code and hook into other features OBP has.