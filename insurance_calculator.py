class InsuranceCalculator:
    def __init__(self, employee):
        self.employee = employee

    def calculate(self):
        # 보험 계산 로직을 만들었습니다. 
        # 예시로 각 보험의 기본 요율을 0.1로 설정했습니다. 
        health_contribution = 0.1
        employment_contribution = 0.1
        industrial_accident_contribution = 0.1
        pension_contribution = 0.1

        results = []
        results.append(f"Health Insurance: {health_contribution}")
        results.append(f"Employment Insurance: {employment_contribution}")
        results.append(f"Industrial Accident Insurance: {industrial_accident_contribution}")
        results.append(f"National Pension: {pension_contribution}")

        return results
