# AI_Healthcare_Diagnosis_Assistant
An AI-powered healthcare diagnosis assistant that predicts diseases based on user-selected symptoms using Cosine Similarity and Streamlit.


Project Overview
-------------------

The AI Healthcare Diagnosis Assistant is a beginner-friendly Artificial Intelligence project developed to predict the most likely diseases based on the symptoms selected by a user.

The goal of this project is not to replace doctors, but to demonstrate how Artificial Intelligence can assist in identifying possible diseases by comparing user symptoms with previously known disease symptom patterns.

This project uses Python, Streamlit, Pandas, NumPy, and Scikit-learn to build a simple yet interactive web application.

Objective
-----------

The main objectives of this project are:

To understand the complete AI project development lifecycle.
To perform data cleaning and preprocessing.
To convert medical symptom data into machine-readable features.
To compare patient symptoms with disease symptom patterns.
To rank diseases based on symptom similarity.
To create a user-friendly healthcare web application using Streamlit.

Technologies Used
-------------------

Technology	    Purpose
Python	        Programming Language
Pandas	        Data Manipulation
NumPy	        Numerical Computation
Scikit-Learn	Cosine Similarity Algorithm
Streamlit	    Web Application
VS Code	        Development Environment

Dataset Information
---------------------

The project uses an Excel dataset containing diseases and their associated symptoms.

Dataset Summary
Total Diseases: 134
Total Symptoms: 401
Dataset Format: Excel (.xlsx)

Initially, the dataset contained duplicate entries and missing values, which were cleaned before building the prediction system.

Data Preprocessing
--------------------

Step 1 – Handle Missing Values
Step 2 – Remove Duplicate Records
Step 3 – Group Symptoms

Feature Engineering
-----------------------

Machine learning models cannot understand text directly.
Therefore, every symptom was converted into binary values.

1 = Symptom Present
0 = Symptom Absent

Machine Learning Approach 
----------------------------

At first, we attempted to solve the problem using a Random Forest Classifier.
Symptoms

↓

Random Forest

↓

Predicted Disease
Unfortunately, the model performed extremely poorly.
The confusion matrix showed that almost every prediction was incorrect.

* Why Did Random Forest Fail? * 

This happened because of the nature of the dataset.
Every disease had only one training sample.
There were 134 different classes but only 134 rows.
During train-test splitting, many diseases appeared only in the testing set and not in the training set.
As a result, the classifier had never seen those diseases before.

*Solution*

Instead of forcing a machine learning classifier, we changed our approach.

Rather than predicting a disease using a trained model, we compared the user's symptoms with every disease already present in the dataset.

This turned the problem into a similarity matching problem.

Chose Cosine Similarity
---------------------------

Cosine Similarity compares two vectors.
The disease having the highest similarity score is considered the best match.

This approach works well because our dataset is essentially a collection of disease symptom profiles rather than a large labeled dataset for training.

User Selects Symptoms

↓

Symptoms Converted into Binary Vector

↓

Cosine Similarity Calculation

↓

Compare with 134 Diseases

↓

Rank Diseases

↓

Display Top 3 Matches


Streamlit Application
------------------------

The project includes an interactive web interface developed using Streamlit.

The application allows users to:

View project statistics
Select symptoms from a searchable list
Predict the top matching diseases
Display similarity scores
View matched symptoms

Acknowledgement
-----------------

This project was developed as a learning project to understand how Artificial Intelligence techniques can be applied in healthcare. 
It demonstrates the complete journey from raw data to a working web application, including data cleaning, feature engineering, 
experimenting with different algorithms, identifying limitations, and selecting a more suitable approach.
