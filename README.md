# **Texas Seeking Transparency in Application to Residency (STAR) Dual Degree Study**

### Author: Daniel Brock
### Date Created: 12/14/2024

## **Purpose**
The goal of this study is to identify applicant characteristics, disparities, and specialty trends among dual degree (MD-PhD, MD-MPH, MD-MBA, and MD-MSc) applicants.

## **Analysis Steps**
1. 01_TexasSTAR_analysis.Rmd - main R markdown file for statistics and data visualization.
   * Source: https://www.utsouthwestern.edu/education/medical-school/about-the-school/student-affairs/texas-star.html 
2. 02_webscraper.ipynb - Jupyter notebook for collecting residency rank data from Doximity.
   * Source: https://www.doximity.com/residency/
3. 03_school_matcher.py - python script to match residency programs by specialty listed in Texas STAR to program names listed in Doximity. Based on fuzzy string matching.