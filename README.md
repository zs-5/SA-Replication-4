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
requirements.txt                 # Python dependencies needed to run the scripts
outputs/
    recall_graph.png             # Recall curve produced by our reproduction, from graph_recall.py
    threshold_recalls.csv        # CSV file containing recall values for thresholds, from BugLearnAndValidate.py
    training_prediction_time.txt # Contains how long (min:sec) extracting pairs, training, and prediction took, from BugLearnAndValidate.py
replication_scripts/
    BugLearnAndValidate.py       # Modified version of the original script (see notes below)
    graph_recall.py              # Plots recall curve from CSV values saved by BugLearnAndValidate.py
```

**Note on `BugLearnAndValidate.py`**: This is a modified version of the original script from the DeepBugs repository. The following changes were made:
- Fixed several bugs present in the original script
- Added timing instrumentation that prints elapsed time for each phase to the console and saves it to a text file
- Added logic to save threshold and recall values to a CSV file, which is consumed by `graph_recall.py` to generate the recall curve, and save training/prediction component timings to `outputs/training_prediction_time.txt`

**Note on data**: The full js150k corpus (150,000 JavaScript files) used for training and validation is not included in this repository due to its size. See the setup instructions below for how to download it.

---

## 3. Setup Instructions

- **Prerequisites**: Python 3.13 (tensorflow doesn't yet support 3.14 or 3.15), 
 
- **Installation Steps**:

    - Clone [michaelpradel/DeepBugs](https://github.com/michaelpradel/DeepBugs)
        ```bash
        $ cd ..
        $ git clone https://github.com/michaelpradel/DeepBugs.git
        $ cd DeepBugs
        ```

    - Obtain dataset
        - Download the full 150k JS dataset from https://www.sri.inf.ethz.ch/js150
        - Extract it, then extract the `data.tar.gz` archive inside it, and copy the `programs_all` folder to the `data/js/` folder of the cloned DeepBugs repo. You should now end up with a populated `programs_all` folder (`data/js/programs_all/0a-`, and so on).

    - Create an `outputs` directory, and overwrite the BugLearnAndValidate.py file in the repo with the version from this repo (`replication_scripts/BugLearnAndValidate.py`).

    - Follow the instructions in the DeepBugs readme to train and validate the model

    - Copy the `outputs` folder to this repo

    - Setup venv and dependencies
        ```bash
        $ python3 -m venv .venv
        $ source .venv/bin/activate
        $ pip3 -r requirements.txt
        ```
    
    - Run `graph_recall.py` to plot the recall graph, and automatically save it to `outputs/recall_graph.png`.
        ```bash
        python3 replication_scripts/graph_recall.py
        ```

---

## 4. GenAI Usage

**Claude (claude.ai)** was used during this replication in the following ways:

- **Report writing**: Claude was used to improve the readability and academic tone of the replication report, including the abstract, introduction, and conclusions sections, and the README.
- **Code understanding**: Claude was used to help understand the structure and logic of the original DeepBugs codebase, particularly the JavaScript call-site extraction scripts and the Python training pipeline, which aided in setting up and running the replication correctly.

No GenAI tool was used to generate experimental results, produce or modify training/evaluation scripts, or conduct the manual analysis of real-world warnings.
