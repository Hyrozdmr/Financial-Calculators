from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Investment Calculator Route
@app.route('/investment', methods=['GET', 'POST'])
def investment():
    if request.method == 'POST':
        try:
            deposit = float(request.form['deposit'])
            rate = float(request.form['rate'])
            time = float(request.form['time'])
            interest_type = request.form['interest']

            if interest_type == 'simple':
                total = deposit * (1 + (rate / 100) * time)
                result = f"Final Total (Simple Interest): £{round(total, 2)}"
            elif interest_type == 'compound':
                total = deposit * math.pow((1 + (rate / 100)), time)
                result = f"Final Total (Compound Interest): £{round(total, 2)}"
            else:
                result = "Invalid interest type selected."
        except ValueError:
            result = "Please enter valid numerical inputs."

        return render_template('result.html', title="Investment Result", result=result)

    return render_template('investment.html', title="Investment Calculator")

# Bond Calculator Route
@app.route('/bond', methods=['GET', 'POST'])
def bond():
    if request.method == 'POST':
        try:
            house_value = float(request.form['house_value'])
            rate = float(request.form['rate'])
            months = int(request.form['months'])

            monthly_rate = (rate / 12) / 100
            repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** -months)
            result = f"Monthly Repayment: £{round(repayment, 2)}"
        except ValueError:
            result = "Please enter valid numerical inputs."

        return render_template('result.html', title="Bond Result", result=result)

    return render_template('bond.html', title="Bond Calculator")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
