from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():

    # Get values from form
    transaction_type = request.form['type']
    amount = float(request.form['amount'])
    oldbalance = float(request.form['oldbalance'])
    newbalance = float(request.form['newbalance'])

    # Fraud Detection Logic
    if amount > oldbalance:
        prediction = "Fraud"

    elif amount > 50000:
        prediction = "Fraud"

    else:
        prediction = "Not Fraud"

    # Send result back to webpage
    return render_template(
        'index.html',
        prediction=prediction
    )


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)