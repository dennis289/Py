# a payroll system for how employees are salaried.
class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id= emp_id
        self.name=name
        self.salary=salary
    def calculate_salary(self):
        pass
#child classes
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, salary,hourly_rate,hours_worked):
        super().__init__(emp_id, name, salary)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        salary=self.hourly_rate*self.hours_worked
        return salary
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name,monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary=monthly_salary
    def calculate_salary(self):
        pass
class CommisionedEmployee(Employee):
    def __init__(self, emp_id, name,commission,goodsSold):
        super().__init__(emp_id, name)
        self.commision= commission
        self.goodsSold=goodsSold
    def calculate_salary(self):
        salary= self.commision/100* self.goodsSold
        return salary