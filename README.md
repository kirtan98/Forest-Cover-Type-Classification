# Forest Cover Type Prediction using scikit-learn Algorithms

## Algorithms and Performance
The algorithms applied in this project include:
- Logistic Regression
- Random Forest Classifier
- Extra Trees Classifier
- Gradient Boosting Classifier
- Decision Tree Classifier

After a thorough evaluation, the RandomForestClassifier emerged as the most effective algorithm for predicting forest cover types. The achieved accuracy score is an impressive 0.845, demonstrating the model's robust predictive capability.

## Optimal Parameters
The optimal hyperparameters for the RandomForestClassifier were determined using GridSearchCV, a technique that systematically explores various hyperparameter combinations to find the best-performing set. The parameters obtained from GridSearchCV for the RandomForestClassifier are as follows:

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
