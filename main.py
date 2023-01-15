from flask import Flask,render_template,request,redirect
app=Flask(__name__)
from function import loan

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data=request.form
    Gender=float(data["Gender"])
    Married=float(data["Married"])
    Dependents=float(data["Dependents"])
    Education=float(data["Education"])
    Self_Employed=float(data["Self_Employed"])
    ApplicantIncome=float(data["ApplicantIncome"])
    CoapplicantIncome=float(data["CoapplicantIncome"])
    LoanAmount=float(data["LoanAmount"])
    Loan_Amount_Term=float(data["Loan_Amount_Term"])
    Credit_History=float(data["Credit_History"])
    Property_Area=data["Property_Area"]

    output=loan(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area).final()
    return render_template("index.html",prediction=output)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)