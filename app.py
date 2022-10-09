from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn import linear_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    Hours_Formatted = 0
    if request.method == "POST":

        grade_percentage = float(request.form.get("gradepercentage"))

        if (grade_percentage > 100):
            grade_percentage = 100

        df = pd.read_excel("/Users/izat/Documents/Projects/DA_Hacks/Grades2.xlsx")

        Regression_Model = linear_model.LinearRegression()

        Regression_Model.fit(df[['Grade percentage']],df['Hours spent per week'])
        Hours = float(Regression_Model.predict([[grade_percentage]]))

        if (Hours < 0):
            Hours = 0

        Hours_Formatted = round(round(Hours,2)*2)/2

        return render_template('index.html', prediction=Hours_Formatted)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)