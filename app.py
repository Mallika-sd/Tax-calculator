from flask import Flask, request, render_template
import tax

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods = ['POST'])
def calculate():
    income = request.form["income"]
    deductions= request.form["deductions"]
    old_tax, new_tax = tax.compare_and_calculate(int(income), int(deductions))
    if new_tax < old_tax:
        Choose = 'New Tax Regime'
        Benefit = old_tax - new_tax
    else:
        Choose = 'Old Tax Regime'
        Benefit = new_tax - old_tax
    return render_template("index.html", ot = old_tax, nt = new_tax, benefit = Benefit, regime = Choose)        

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
