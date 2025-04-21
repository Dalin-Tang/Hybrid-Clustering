# Hybrid-Clustering

# DBSCAN-Natural Break Hybrid Clustering for Traffic State Classification

## Project Overview

This project implements a hybrid clustering approach combining **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) and **Natural Breaks** to classify traffic states. The clustering algorithm processes traffic speed data to determine the relative speed thresholds, speed statistics, and the correlation coefficients of adjacent road segment thresholds. The methodology aims to enhance the understanding of traffic flow and congestion patterns.

### Files in This Project

This project consists of the following files:

1. **`indx_wf_relapartion_DBSACN_NaturalBreaks.py`**  
   This is the main program file that integrates the fusion clustering algorithm. It outputs:
   - The relative speed thresholds for traffic state classification.
   - Statistical metrics of relative speed.
   - Correlation coefficients between adjacent thresholds for all road segment samples.

2. **`test.py`**  
   This file serves as the testing script for the project. It runs the clustering process and outputs the classification results.

3. **`output.txt`**  
   This file contains the results of the tests run on the dataset, including the traffic state classifications, relative speed thresholds, and the correlation between adjacent road segment thresholds.

4. **`raw_data_sample`**  
   A sample of raw traffic data. The columns are:
   - `cityname`: Name of the city.
   - `ds`: Date.
   - `time_interval`: Time interval of data collection.
   - `seg_id`: Road segment ID.
   - `speed`: Recorded speed of the segment.

5. **`bj_test`**  
   This is a processed version of the raw data, which can be directly input into the program. The columns are:
   - `seg_id`: Road segment ID.
   - `speed`: Recorded speed of the road segment.

## Usage

### Requirements

- Python 3.9
- Required libraries:
  - `numpy`
  - `pandas`
  - `sklearn`
  - `matplotlib`
  - `scipy`
  - `jenkspy`
  - `os`

Install the necessary dependencies with:

```bash
pip install -r requirements.txt
```

### Running the Program

1. Place your data in the correct format (see `bj_test` for an example).
2. Run the clustering algorithm using the `indx_wf_relapartion_DBSACN_NaturalBreaks.py` file.
   ```bash
   python indx_wf_relapartion_DBSACN_NaturalBreaks.py
   ```
3. The results will print the traffic state classification and analysis.

### Testing

To test the program with a sample dataset, run the `test.py` file:

```bash
python test.py
```

This will print an output ,you can compare it with file (`output.txt`).

## Results

After running the program, the output will contain the following results:
- The relative speed thresholds for classifying traffic states.
- The statistical metrics of relative speed.
- The correlation coefficients between the thresholds of adjacent road segments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


