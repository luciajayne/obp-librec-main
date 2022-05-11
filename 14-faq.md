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

### How important are rewards in OBP?
OBP is more concerned about the reward because it makes recommendations of that. 

### What is IPW?
Inverse Probability weighting (IPW) means that if there is data missing, it reduces the weight of those missing items. But, it increases the data of the users that are there for future allocations. 

### What is the item_ID in IPWLearner?
The learner expands the item_ID to a vector field (vectorizes the item). It takes value of item_ID and converts it into ones and zeros. That vector then is used as the action in OBP.
 
### What is OBP input and output for this project?
The input should be user_ID and the output should be a list.

### What is the advantage of using OBP?
The advantage of OBP is to use code and hook into other features OBP has.
