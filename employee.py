
#사원번호 클래스

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

        #사원번호를 불러올 수 있도록 하는 함수입니다. 

    def get_info(self):
        return f"이름: {self.name}, 사원번호: {self.employee_id}"
