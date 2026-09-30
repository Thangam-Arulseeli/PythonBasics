from employee import Employee

def test_calculate_bonus():
    emp = Employee("Arun", 50000)

    result = emp.calculate_bonus()

    assert result == 5000


def test_high_earner():
    emp = Employee("Arun", 60000)

    result = emp.is_high_earner()
                                           
    assert result is True


def test_not_high_earner():
    emp = Employee("Kumar", 30000)

    result = emp.is_high_earner()

    assert result is False


# def test_is_high_earner():
#     emp1 = Employee("Arun", 50000)
#     emp2 = Employee("Bob", 40000)

#     assert emp1.is_high_earner() == True
#     assert emp2.is_high_earner() == False

