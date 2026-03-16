# **Texas Seeking Transparency in Application to Residency (STAR) Dual Degree Study**

### Author: Daniel Brock
### Date Published: 2/19/2026

## **Citation**
View the publication on JCI Insight: https://insight.jci.org/articles/view/198778

Please cite us: Brock DC, Rupert DD, Darville T, Jansen CS, Wisdom EM, Tang CY. Dual-degree pathways in the residency match: a comparative analysis of application behaviors and outcomes. JCI Insight. Published 2026 Feb 19. [https://doi.org/10.1172/jci.insight.198778 ](https://insight.jci.org/articles/view/198778)

## **Purpose**
The goal of this study is to identify applicant characteristics, disparities, and specialty trends among dual degree (MD-PhD, MD-MPH, MD-MBA, and MD-MSc) applicants.

## **Analysis Steps**
1. 01_TexasSTAR_analysis.Rmd - main R markdown file for statistics and data visualization.
   * Source: https://www.utsouthwestern.edu/education/medical-school/about-the-school/student-affairs/texas-star.html 
2. 02_Doximity_ranker.ipynb - Jupyter notebook for collecting residency rank data from Doximity.
   * Source: https://www.doximity.com/residency/
3. 03_school_matcher.py - python script to match residency programs by specialty listed in Texas STAR to program names listed in Doximity. Based on fuzzy string matching.
4. 04_school_matcher.ipynb - Jupyter notebook for concatenating and cleaning all matched names from Doximity and Texas STAR.
5. 05_random_forest.ipynb - Jupyter notebook modeling a random forest classifier to determine feature importance for different degree paths. No longer used in main paper.
6. 06_XGBoost.ipynb - Jupyter notebook utilizing an XGBoost regressor to determine feature importance for predicting number of interview offers and residency program rank. No longer used in main paper.
7. 07_BlueRidge_rankings.ipynb - Jupyter notebook for matching programs ranked by Blue Ridge to TexasSTAR.