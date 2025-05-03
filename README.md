# Hybrid-Clustering

## DBSCAN-Natural Break Hybrid Clustering for Traffic State Classification

### Project Overview

This project implements a hybrid clustering approach combining **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) and **Natural Breaks (Jenks)** to classify traffic states. The algorithm is designed to extract meaningful traffic patterns from speed data across road segments by determining relative speed thresholds for various traffic states and analyzing the inter-segment relationships in traffic behavior.

The main functions include:
- Determining relative speed thresholds for traffic state classification using hybrid clustering.
- Computing statistical metrics (mean, standard deviation, etc.) of relative speeds in each cluster.
- Analyzing the correlation of traffic states between adjacent road segments, including:
  - Linear regression slope and intercept.
  - Pearson correlation coefficient (R).
  - p-value of statistical significance.
  - Standard error of regression coefficients.

---

### Files in This Project

1. **`indx_wf_relapartion_DBSACN_NaturalBreaks.py`**  
   The main script that implements the hybrid clustering and correlation analysis. It outputs:
   - Traffic state classifications based on relative speed thresholds.
   - Statistical summaries for each traffic state.
   - Correlation metrics between adjacent segments, including regression parameters and statistical significance.

2. **`test.py`**  
   A test script for verifying the clustering and correlation process on sample data. It prints the classification results and correlation coefficients.

3. **`output.txt`**  
   Contains the output results:
   - Relative speed thresholds by traffic state.
   - Traffic state classification of sample segments.
   - Correlation analysis results between adjacent road segment thresholds.

4. **`raw_data_sample`**  
   Sample input data in raw form, with the following columns:
   - `cityname`: Name of the city.
   - `ds`: Date.
   - `time_interval`: Time interval of data collection.
   - `seg_id`: Road segment ID.
   - `speed`: Measured speed of the segment.

5. **`bj_test`**  
   A processed data file ready for direct input into the program, with:
   - `seg_id`: Road segment ID.
   - `speed`: Speed observation.

---

### Usage

#### Requirements

- Python 3.9+
- Required libraries:
  - `numpy`
  - `pandas`
  - `sklearn`
  - `matplotlib`
  - `scipy`
  - `jenkspy`
  - `os`

Install all dependencies with:

```bash
pip install -r requirements.txt

Running the Program
	1.	Prepare your dataset in the required format (see bj_test).
	2.	Run the main clustering and correlation analysis script:

python indx_wf_relapartion_DBSACN_NaturalBreaks.py

	3.	The results will include traffic state classification and correlation analysis between adjacent segments.

Testing

To test with provided sample data, use:

python test.py

The output can be compared with the contents of output.txt.

⸻

Results

The program outputs the following:
	•	Traffic state classifications for each road segment.
	•	Relative speed thresholds for each traffic state.
	•	Statistical summaries of relative speeds within each state.
	•	Correlation analysis results for adjacent segments, including:
	•	Regression slope and intercept.
	•	Correlation coefficient (R).
	•	p-value from hypothesis testing.
	•	Standard error of regression coefficients.

These results provide insight into not only the classification of traffic conditions but also the spatial relationships and dependencies between neighboring road segments.
