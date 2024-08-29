from flask import Flask, request
import pickle
import sklearn


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Loan Approval Testing using flask</p>"

@app.route("/ping", methods=['GET'])
def pinger():
    return "<p>Routing works</p>"

@app.route("/json", methods=['GET'])
def json_check():
    return {"message": "Hi i am json!"}

model_pickle = open("./artifacts\classifier.pkl", "rb")
clf = pickle.load(model_pickle)

@app.route("/predict", methods=['POST'])
def prediction():
    loan_req = request.get_json()


    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Yes":
        Married = 1
    else:
        Married = 0
    
    if loan_req['Credit_History'] == "Cleared Debts":
        Credit_History = 1
    else:
        Credit_History = 0
    

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']


    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}
    

   