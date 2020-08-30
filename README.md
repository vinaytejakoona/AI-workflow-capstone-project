# AI workflow Capstone project!

## EDA
EDA analysis with visualizations is in the jupyter notebook

## Model Selection
Tried out multiple models, The code for training gradient boosting and random forest ensemble methods is in model.py. Random forest model is chosen based on lower error and integrated into API.

## Test cases
  Used unittest module for writing unit test cases.
  written unit tests for the API, model, logging.
  All unit test cases can be run with single command
 >   python run-tests.py

## Monitoring Performance
model's error is logged to train logs to track model prediction performance.
runtime of each prediction is logged to log files to keep track of model runtime performance.

## Built a flask app to expose API
model can be trained using an API call. predictions can also be obtained by passing country, year, month, day parameters.

## Containerized the application
Dockerfile is included to build the  image.
