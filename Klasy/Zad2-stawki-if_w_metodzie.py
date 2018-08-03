# Zadanie 2
# Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
# pracy oraz wypłacanie pensji na podstawie zadanej stawki godzinowej.
# Jeżeli pracownik będzie pracował więcej niż 8 godzin
# (podczas pojedynczej rejestracji czasu) to kolejne godziny
# policz jako nadgodziny (z podwójną stawką godzinową)

class Employee:
    def __init__(self, first_name, last_name, rate_per_hour):
        self.first_name = first_name
        self.last_name = last_name
        self. rate_per_hour = rate_per_hour
        self._registered_normal_hours = 0
        self._registered_overtime_hours = 0

    def pay_salary(self, hours):
        if hours <=8:
            self._registered_normal_hours += hours
        else:
            self._registered_normal_hours = 8
            self._registered_overtime_hours = hours - 8

        payment = self._registered_normal_hours *\
                  self.rate_per_hour + \
                  self._registered_overtime_hours*\
                  self.rate_per_hour * 2

        self._registered_normal_hours = 0
        self._registered_overtime_hours = 0

        print(f'{self.first_name} {self.last_name} - wypłata: {payment}')
        return payment

employee = Employee('Jan', 'Nowak', 100)

employee.pay_salary(11)