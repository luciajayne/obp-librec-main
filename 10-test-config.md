---
layout: default
title: Testing Configurations
nav_order: 10
---
# Configurations
## Librec-auto Configuration File
LibRec Auto takes a configuration file, then splits the data, then recommendations, then evaluations.
![librec-auto config](content/configurations/librec-auto_conf.png)
1. Data section: Uploads the data.
![data_conf](content/configurations/librec-auto/data_conf.png)
2. Feature section: Enumerates the features and pin the features to the dataset.
![fea_config](content/configurations/librec-auto/fea_conf.png)
3. Splitter section: not applicable for this project.
![splitter_config](content/configurations/librec-auto/splitter_conf.png)
4. Algorithm section: Responsible for taking the features and give the recommendation list.
![alg_config](content/configurations/librec-auto/alg_conf.png)
5. Rerank section: Necessary for SCRUF-D project.
![rerank_config](content/configurations/librec-auto/rr_conf.png)

*Other sections: metrics (measurement), post-processing (for excel, or browser).*

## PyCharm Testing Configuration Examples

### OBP Demo OFAiR Configuration
![obp_demo_ofair](content/configurations/obpfair_conf.png)

### OBP OFAiR Reranker Configuration
![](content/configurations/obp_rr_conf.png)
