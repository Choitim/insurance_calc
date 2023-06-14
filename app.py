from flask import Flask, render_template, request #웹 flask를 활용해서 html 페이지를 랜더링 합니다. 

app = Flask(__name__)


# 보험 계산기 클래스
class InsuranceCalculator:
    def __init__(self, salary, insurance_rate):
        self.salary = salary
        self.insurance_rate = insurance_rate

# 보험 계산기. 
    def calculate_insurance(self):
        health_insurance = self.salary * self.insurance_rate / 100
        employment_insurance = self.salary * 0.8 / 100
        pension_insurance = self.salary * 9.5 / 100
        national_pension = self.salary * 4.5 / 100
        total_insurance = health_insurance + employment_insurance + pension_insurance + national_pension
        return {
            'health_insurance': health_insurance,
            'employment_insurance': employment_insurance,
            'pension_insurance': pension_insurance,
            'national_pension': national_pension,
            'total_insurance': total_insurance
        }
    

    # html 페이지 랜더링. POST 결과 시 결과물 출력

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        salary = int(request.form['salary'])
        insurance_rate = float(request.form['insurance_rate'])

        calculator = InsuranceCalculator(salary, insurance_rate)
        result = calculator.calculate_insurance()

        return render_template('index.html', result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
