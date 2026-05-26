from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    amount = float(request.form['amount'])

    # Fraud logic
    if amount > 1000:
        prediction = "Fraud"
    else:
        prediction = "Not Fraud"

    return render_template(
        'index.html',
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)