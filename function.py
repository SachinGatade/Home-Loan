import json,pickle
import numpy as np

class loan():
    def __init__(self,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
        self.Gender=Gender
        self.Married=Married
        self.Dependents=Dependents
        self.Education=Education
        self.Self_Employed=Self_Employed
        self.ApplicantIncome=ApplicantIncome
        self.CoapplicantIncome=CoapplicantIncome
        self.LoanAmount=LoanAmount
        self.Loan_Amount_Term=Loan_Amount_Term
        self.Credit_History=Credit_History
        self.Property_Area=Property_Area
        
    def input_data(self):
        with open("dt_model.pickle","rb") as f:
            self.model=pickle.load(f)

        with open("standard_scale.pickle","rb") as f:
            self.std_scale=pickle.load(f)

        with open("feature.json","r") as f:
            self.col_list=json.load(f)

    def final(self):
        self.input_data()

        arr=np.zeros(len(self.col_list["columns"]))

        arr[0]=self.Gender
        arr[1]=self.Married
        arr[2]=self.Dependents
        arr[3]=self.Education
        arr[4]=self.Self_Employed
        arr[5]=self.ApplicantIncome
        arr[6]=self.CoapplicantIncome
        arr[7]=self.LoanAmount
        arr[8]=self.Loan_Amount_Term
        arr[9]=self.Credit_History

        area="Property_Area_"+self.Property_Area
        index_name=self.col_list["columns"].index(area)
        arr[index_name]=1.0

        arr_data=self.std_scale.transform([arr])

        result=self.model.predict(arr_data)
        return result
