---
layout: default
title: OFAiR Metrics
nav_order: 9
---
[Librec-auto: ofair_rerank.py](https://github.com/that-recsys-lab/librec-auto/blob/master/librec_auto/core/cmd/rerank/ofair_rerank.py) <br />

**[OFAiR_Paper](content/papers/OFAIR_Paper.pdf) Results** <br />
![OFAiR Results](content/ofair/ofair_ndcg.png)

**Revised Logic Cleaning @50 with obp_rerank.py** <br />
OBP just gives the OFAiR metrics. OBP should give me the same items, and positions for each items (it doesn’t change). <br />
*SAME METRICS WITH OFAIR_RERANK.PY*
![NDCG@10 Results](content/ofair/results_50.png)

**Similar to Sonboli's OFAiR paper data cleaning @10 with ofair_rerank.py** <br />
![N@10 Results](content/ofair/n_10.png)

**Similar to Sonboli's OFAiR paper data cleaning @50 with ofair_rerank.py** <br />
![N@50 Results](content/ofair/n_50.png)
