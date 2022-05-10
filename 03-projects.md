---
layout: default
title: Development
nav_order: 3
---

**Data Cleaning**

[OFAiR Data Cleaning Notebook](https://github.com/luciajayne/obp-librec-main/blob/main/content/OFAiR_Paper_Replication.ipynb) This notebook cleans the data similar to Sonboli’s cleaning data process (derived from Sonboli’s OFAiR project). <br />
[Sonboli's OFAiR Github](https://github.com/nasimsonboli/OFAiR/blob/main/source%20code/ML26_data_prep.ipynb)

**Running Librec-auto**

[Install Librec-auto](https://librec-auto.readthedocs.io/en/latest/index.html) <br />
[Download Pycharm Community Version](https://www.jetbrains.com/pycharm/download/#section=windows)

**OBP Trainer** 

[OBP Trainer Notebook](content/OBP_Trainer.ipynb)
Developed to provide a proof of concept. The learner uses the pass-through policy to take in as context user_ID in order to predict a Recommendation List. Similar results can be achieved by using a classification model. <br />
*1 user_ID → 1 recommendation list (is the nature of the design). This is somewhat impractical because the size of the resulting pickle file (i.e it is 44GB for the movie dataset). In other words, hard to scale.* <br />

*How OBP stores data for the specific MovieDataSet*
```Python
 'n_actions': 2830, # number of uniques itemids
    'context': array([0,1,2,3,4,5,...]), #userID
     #one action (itemID) for each position or 50*len(context)
    'action': array([8, 6, 5, 4, 7, 0, 1, 3, 5, 4, 6, 1, 4, 1, 7,...]), 
     #up to 50 positions for each context or 50*len(context)
    'position': array([0, 1, 2…49,50, 0, 1, 2…49,50,0, 1, 2…49,50,...]), 
 'reward': array([1, 1, 1, ..., 1, 1, 1]), #set all rewards to one
```
*OBP: replace ofair_rerank.py with obp_rerank.py* <br />
```XML
<!-- RERANK SECTION -->
  <rerank>
    <script lang="python3" src="system">
	<script-name>obp_rerank.py</script-name> 
	<param name="max_len">50</param>
	<param name="lambda"><value>0.9</value></param>
	<param name="binary">False</param>
	<param ref="fea:new"/>
    </script>
  </rerank>
```
**Results** <br />
Found in folder DemoOFAiR/Exp00000/result
The results for the movie dataset differ from Sonboli’s OFAiR paper because the author used different metrics code [Sonboli OFAiR Repository](https://github.com/nasimsonboli/OFAiR/blob/main/source%20code/ML26_data_prep.ipynb) *Librec-auto wasn’t used to calculate Sonboli's metrics*. 

**OBP Exporter** <br />
Input: demoX-out-1.txt <br />
Output: IPW_OBP_demoX.pickle <br />
[OBP Exporter Notebook](https://github.com/luciajayne/obp-librec-main/blob/main/content/OBP_Exporter.ipynb)

**DEMO OBP Projects** <br />
The changes were made to the algorithm section of librec-auto. It was replaced with OBP. They require a pickle file (use the OBP Exporter notebook to create a pickle file).
The following demo OBP projects:
1. DemoOBP_STANDARD
2. DemoOBP_RANDOM
3. DemoOBP_FAIR
4. DataOFAiR: was bult from the movie data. It contains the notebook to prepare the data. The movie data source is Kaggle. 
5. DemoOFAiR: changes to the re-ranking section two options: obp_rerank.py(added 04-2022) or ofair_rerank.py (already built-in librec-auto)
6. DemoMMR: extension of OFAiR (same as OFAiR reranking but it uses MMR: already built-in librec-auto).
<br />
*Built-in demos on Librec-auto* <br />
Demo 01 to Demo 05: come built-in with Librec-auto

**OBP** <br />
[OBP Github](https://github.com/st-tech/zr-obp) <br />
OBP Tutorial by the authors
<iframe width="187" height="105" src="https://www.youtube.com/embed/HMo9fQMVB4w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
