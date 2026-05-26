from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    amount = float(request.form['amount'])
oldbalance = float(request.form['oldbalance'])
newbalance = float(request.form['newbalance'])

if amount > oldbalance:
    result = "Fraud"
elif amount > 50000:
    result = "Fraud"
else:
    result = "Not Fraud"

return render_template("index.html", prediction=result)
    

if __name__ == "__main__":
    app.run(debug=True)