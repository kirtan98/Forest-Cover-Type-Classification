# Forest Cover Type Prediction using scikit-learn Algorithms

This project focuses on predicting forest cover types using a variety of classification algorithms provided by the scikit-learn library in Python. The algorithms utilized in this project are:

- Logistic Regression: A linear classification algorithm often used for binary and multi-class classification tasks.

- Random Forest Classifier: An ensemble method that builds multiple decision trees and combines their predictions for improved accuracy and reduced overfitting.

- Extra Trees Classifier: Similar to Random Forest, Extra Trees builds multiple decision trees with random splits to enhance diversity among trees.

- Gradient Boosting Classifier: An ensemble technique that builds decision trees sequentially to correct errors of the previous models, leading to higher accuracy.

- Decision Tree Classifier: A basic algorithm that creates a decision tree by recursively partitioning the feature space based on specific criteria.

## Best Algorithm and Performance
Following a thorough evaluation, the RandomForestClassifier emerged as the optimal algorithm for Forest Cover Type prediction in this project. The achieved accuracy score is an impressive 0.845, signifying the algorithm's robust predictive capability.

## Optimal Parameters
The best parameters for achieving this high accuracy score with the RandomForestClassifier are as follows:

bootstrap: True
class_weight: 'balanced'
criterion: 'entropy'
max_features: 'auto'
min_samples_leaf: 1
min_samples_split: 2
n_estimators: 500

## Reference:
### Dataset Source
Visit https://www.kaggle.com/c/forest-cover-type-prediction/data
### Forest Cover Type Classification Study- Thomas Kolasa and Aravind Kolumum Raja
Visit https://rstudio-pubs-static.s3.amazonaws.com/160297_f7bcb8d140b74bd19b758eb328344908.html
