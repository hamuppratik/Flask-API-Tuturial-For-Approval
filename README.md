# Learning Model deploment Using Flask

In this project, I worked on deploying a machine learning model that I previously created, named "loantap_personal_loan_creditworthiness_modeling." This model is a classification model designed to determine whether a loan should be approved or rejected. It takes input data in JSON format, which includes details like the applicant's gender, marital status, income, credit history, and loan amount.

Here's a simple breakdown of what I did:

Imported necessary libraries: I used Flask for creating the API, pickle to load the model, and sklearn for handling the model’s predictions.

Set up Flask routes:

Home route ("/"): Displays a simple message indicating that the loan approval testing is done using Flask.
Ping route ("/ping"): Just a check to ensure the routing is working properly.
JSON check route ("/json"): Returns a basic JSON message for testing.
Loaded the model: I opened and loaded the pre-trained model (classifier.pkl) using pickle.

Created a prediction route ("/predict"):

Input Processing: I defined how the input JSON should be processed. I converted categorical data like gender, marital status, and credit history into numerical values that the model can understand.
Prediction: I passed these processed inputs into the model to predict whether the loan should be approved or rejected.
Output: The output is a JSON response with the loan approval status, either "Approved" or "Rejected."
I tested the API using Flask and Postman to ensure everything works smoothly. The final output of the model looks like this:

 ```{
    "loan_approval_status": "Rejected"
} ```


This project effectively demonstrates how to deploy a machine learning model as a web service, allowing others to make predictions using the model via an API..