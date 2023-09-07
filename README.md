# Forest Cover Type Prediction using scikit-learn Algorithms

This repository contains a machine learning project focused on predicting forest cover types using various classification algorithms from the scikit-learn library. The dataset used for this project is the Kaggle Forest Cover Type dataset.

## Algorithms Explored

- Logistic Regression
- Random Forest Classifier
- Extra Trees Classifier
- Gradient Boosting Classifier
- HistGradient Boosting Classifier
- Decision Tree Classifier

## Best Algorithm and Hyperparameters

After thorough experimentation, the RandomForestClassifier was found to be the best-performing algorithm for this task. The optimal hyperparameters for the RandomForestClassifier were identified using GridSearchCV, resulting in an accuracy of 0.845.

Best Parameters:
- bootstrap: True
- class_weight: balanced
- criterion: entropy
- max_features: auto
- min_samples_leaf: 1
- min_samples_split: 2
- n_estimators: 500

## Stacking Classifier Experiment 
To further enhance our predictive model, we implemented a Stacking Classifier. We conducted experiments in four different cases to assess its performance:
### Case 1: All Algorithms with Their Hyperparameters
- Base Classifiers:
  - LogisticRegression
  - ExtraTreesClassifier
  - DecisionTreeClassifier
  - GradientBoostingClassifier
  - HistGradientBoostingClassifier
- Meta-Classifier:
  - RandomForestClassifier

### Case 2: Ensemble Algorithms with Their Hyperparameters
- Base Classifiers:
  - ExtraTreesClassifier
  - GradientBoostingClassifier
  - HistGradientBoostingClassifier
- Meta-Classifier:
  - RandomForestClassifier

### Case 3: Best Accuracy Algorithms with Their Hyperparameters
- Base Classifiers:
  - ExtraTreesClassifier
  - GradientBoostingClassifier
  - DecisionTreeClassifier

- Meta-Classifier:
  - RandomForestClassifier
### Case 4: Algorithms with Their Hyperparameters

- Base Classifiers:
  - LogisticRegression
  - RandomForestClassifier
  - DecisionTreeClassifier
  - GradientBoostingClassifier

- Meta-Classifier:
  - ExtraTreesClassifier

#### Results

After conducting these experiments, we found that **Case 1** yielded the best results:

- Model Accuracy: 0.8596
- Test Data Accuracy: 0.8585

This case involved using all algorithms with their respective hyperparameters as base classifiers and a RandomForestClassifier as the meta-classifier. It achieved the highest accuracy on our dataset.

Feel free to explore the experiment details and results in more depth within this repository. You can find the code, data, and additional information in the project's files.

## Reference:
### Dataset Source
Visit https://www.kaggle.com/c/forest-cover-type-prediction/data
### Forest Cover Type Classification Study- Thomas Kolasa and Aravind Kolumum Raja
Visit https://rstudio-pubs-static.s3.amazonaws.com/160297_f7bcb8d140b74bd19b758eb328344908.html
