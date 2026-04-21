# Replication of "DeepBugs: A Learning Approach to Name-based Bug Detection"

**Course**: CS-UH 3260 Software Analytics, NYUAD  
**Instructor**: Dr. Sarah Nadi

---

## 1. Project Overview

- **Paper Title**: DeepBugs: A Learning Approach to Name-based Bug Detection
- **Original Authors**: Michael Pradel, Koushik Sen
- **Replication Team**: John Yun Moe (jy4017@nyu.edu), Zavier Shaikh (zs2838@nyu.edu)
- **Course**: CS-UH 3260 Software Analytics, NYUAD

**Original Paper Summary**: DeepBugs is a machine learning framework for detecting name-based bugs in JavaScript source code. It formulates bug detection as a binary classification problem, using Word2Vec embeddings to capture semantic similarities between identifiers and a feedforward neural network to distinguish correct from incorrect code. Negative training examples are generated automatically by applying simple code transformations (e.g., swapping function arguments) to existing correct code, removing the need for manual labeling.

**Replication Summary**: We replicate the swapped function arguments bug detector from Section 5.4 of the original paper, using the full js150k corpus of 150,000 JavaScript files — 100,000 for training and 50,000 for validation — matching the original study's setup exactly. We reproduce the accuracy and recall experiments, compare training and inference efficiency against the original Table 6, and additionally apply the trained model to 10 JavaScript files from popular open-source repositories to assess real-world precision through manual analysis.

---

## 2. Repository Structure

```
README.md                        # This file
datasets/                        # Data used in the replication
    file_list_train.txt          # List of 100,000 JS files used for training
    file_list_val.txt            # List of 50,000 JS files used for validation
    download_instructions.md     # Instructions for downloading the full js150k corpus
    real_world_files/            # The 10 JS files used for the inference experiment
replication_scripts/             # Scripts used in this replication
    BugLearnAndValidate.py       # Modified version of the original script (see notes below)
    extract_calls.sh             # Shell script to run JS call-site extraction
    train.sh                     # Shell script to run embedding training + classifier training
    predict.sh                   # Shell script to run inference on new files
    plot_recall.py               # Script to plot recall curve from saved CSV values
outputs/                         # Generated results
    embeddings/                  # Trained Word2Vec embeddings
    model/                       # Trained classifier weights
    predictions/                 # Raw model output (probabilities per call site)
    accuracy_results.txt         # Accuracy with random and learned embeddings
    timing_results.txt           # Timing results for training and prediction phases
    recall_values.csv            # Threshold and recall values used to generate recall curve
    recall_graph.png             # Recall curve (our reproduction)
    recall_graph_og.png          # Recall curve from original paper (for comparison)
    real_world_warnings.csv      # Warnings produced on the 10 real-world JS files
logs/                            # Console output and run logs
    extraction_log.txt           # Output from call-site extraction step
    training_log.txt             # Output from embedding + classifier training
    prediction_log.txt           # Output from inference run
notes/                           # Notes taken during replication
    discrepancies.md             # Notes on any differences observed vs. original paper
    manual_analysis.md           # Notes from manually analyzing the 10 real-world warnings
```

**Note on `BugLearnAndValidate.py`**: This is a modified version of the original script from the DeepBugs repository. The following changes were made:
- Fixed several bugs present in the original script
- Added timing instrumentation that prints elapsed time for each phase to the console and saves it to `outputs/timing_results.txt`
- Added logic to save threshold and recall values to `outputs/recall_values.csv`, which is consumed by `plot_recall.py` to generate the recall curve

---

## 3. Setup Instructions

- **Prerequisites**: Required software, tools, and versions
  - OS requirements
  - Programming language versions (Python, R, etc.)
  - Required packages/libraries and versions
  - Any other dependencies
- **Installation Steps**: Step-by-step instructions to set up the environment
  - How to install dependencies
  - How to configure paths or settings
  - Any environment variables needed

---

## 4. GenAI Usage

**Claude (claude.ai)** was used during this replication in the following ways:

- **Report writing**: Claude was used to improve the readability and academic tone of the replication report, including the abstract, introduction, and conclusions sections, and the README.
- **Code understanding**: Claude was used to help understand the structure and logic of the original DeepBugs codebase, particularly the JavaScript call-site extraction scripts and the Python training pipeline, which aided in setting up and running the replication correctly.

No GenAI tool was used to generate experimental results, produce or modify training/evaluation scripts, or conduct the manual analysis of real-world warnings.
