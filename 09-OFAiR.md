---
layout: default
title: OFAiR Results
nav_order: 9
---

**[OFAiR_Paper](content/papers/OFAIR_Paper.pdf) Results** <br />
![OFAiR Results](content/ofair/ofair_ndcg.png)

**Revised Logic Cleaning @50 with [Librec-auto: ofair_rerank.py](https://github.com/that-recsys-lab/librec-auto/blob/master/librec_auto/core/cmd/rerank/ofair_rerank.py)** <br />
OBP just gives the OFAiR metrics. OBP should give me the same items, and positions for each items (it doesn’t change). <br />
*SAME METRICS WITH OFAIR_RERANK.PY*
![NDCG@10 Results](content/ofair/results_50.png)

**Similar to Sonboli's OFAiR paper data cleaning @10 with [Librec-auto: ofair_rerank.py](https://github.com/that-recsys-lab/librec-auto/blob/master/librec_auto/core/cmd/rerank/ofair_rerank.py)** <br />
![N@10 Results](content/ofair/n_10.png)

**Similar to Sonboli's OFAiR paper data cleaning @50 with [Librec-auto: ofair_rerank.py](https://github.com/that-recsys-lab/librec-auto/blob/master/librec_auto/core/cmd/rerank/ofair_rerank.py)** <br />
![N@50 Results](content/ofair/n_50.png)

**Additional Notes**
1. The [OFAiR Data Cleaning Notebook](https://github.com/luciajayne/obp-librec-main/blob/main/content/OFAiR_Paper_Replication.ipynb) calculates the values as [Sonboli's OFAiR Github](https://github.com/nasimsonboli/OFAiR/blob/main/source%20code/ML26_data_prep.ipynb)
2. The current algorithm and evaluation needs to be integrated to Librec-auto or OBP with enough customization that the hard coded parameters can be easily configured.
3. The metrics (i.e NDCG) calculated using [OBP_rerank.py](content/obp_rerank.py) and [Librec-auto: ofair_rerank.py](https://github.com/that-recsys-lab/librec-auto/blob/master/librec_auto/core/cmd/rerank/ofair_rerank.py).
