# AI-4-UX - Data Cleaning and Analysis Repository

This repository contains a collection of Python scripts and CSV files used for data cleaning, transformation, and statistical analysis. The workflow includes preprocessing open-ended responses, normalizing data, computing statistical measures, and generating correlation matrices.

## Repository Structure

### **Data Cleaning Scripts**
- **`cleanup.py`** – Cleans and processes structured data, ensuring uniform column names and removing unnecessary entries.
- **`scale_mappings.py`** – Maps scale-based responses to numerical values.
- **`convert_to_numbers.py`** – Converts categorical survey responses into numerical values for analysis.

### **Statistical Analysis Scripts**
- **`shapiro_wilk.py`** – Performs a Shapiro-Wilk test to assess normality in the dataset.
- **`spearman.py`** – Computes Spearman’s correlation and generates a heatmap visualization.
- **`skewness_kurtosis.py`** – Computes skewness and kurtosis values for evaluating data distribution.
- **`iqr_median.py`** – Computes median and interquartile range (IQR) to understand data spread.

### **Qualitative Script**
- **`clean_open.py`** – Cleans open-ended responses by merging multiline answers, removing unwanted values, and formatting the text.
- **`translate.py`** – Translates open-ended responses from French to English using `deep_translator`.
- **`feature.py`** – Extracts key features from the dataset for further statistical analysis.1
- **`themes.py`** – Extracts key themes from the dataset for further statistical analysis.1

1 **`feature.py`** and **`themes.py`** should not be considered reliable as the extraction is limited to the keywords set in the script. Please avail human analysis for features and themes.

### **CSV Data Files**
- **`open_ended.csv`** – Raw open-ended responses before cleaning.
- **`open_ended_cleaned.csv`** – Cleaned open-ended responses after text processing.
- **`open_ended_translated.csv`** – Translated open-ended responses (French → English).
- **`your_data.csv`** – Main dataset containing survey responses.
- **`your_data+openended.csv`** – Combined dataset including structured and open-ended responses.
- **`data_no_outliers.csv`** – Preprocessed dataset with outliers removed.
- **`features.csv`** – Extracted features from the dataset.
- **`median_iqr_results.csv`** – Computed median and IQR values.
- **`normality_test_results.csv`** – Results of the Shapiro-Wilk normality test.
- **`skewness_kurtosis_results.csv`** – Skewness and kurtosis analysis results.
- **`spearman_correlation.csv`** – Spearman’s correlation matrix.
- **`spearman_correlation_heatmap.png`** – Heatmap visualization of Spearman's correlation.
- **`themes.csv`** – Processed thematic analysis results.

## Usage

1. **Data Cleaning & Preparation**
   - Run `cleanup.py` to standardize structured data.
   - Use `convert_to_numbers.py` and `scale_mappings.py` to transform categorical responses into numerical values.

2. **Statistical Analysis**
   - Run `shapiro_wilk.py` for normality tests.
   - Run `spearman.py` for correlation analysis.
   - Run `skewness_kurtosis.py` for distribution analysis.
   - Use `iqr_median.py` for median and IQR computations.
  
3. **Preprocessing Open-Ended Responses**
   - Run `clean_open.py` to clean open-ended responses.
   - Run `translate.py` to translate responses into English.
   - Run `feature.py` to extract the key features.
   - Run `themes.py` to extract the key themes.

## Requirements
To run these scripts, install the required dependencies using:

```bash
pip install pandas numpy scipy matplotlib seaborn deep_translator
```

## Contributions
Feel free to contribute by submitting pull requests to improve data processing and analysis workflows.

## License
This project is open-source and licensed under the MIT License.
