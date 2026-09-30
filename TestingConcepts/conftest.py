#  Fixture for creating an Employee instance
import pytest

from employee import Employee

@pytest.fixture
def employee():

    return Employee(
        "Arun",
        "arun@gmail.com",
        50000
    )
    # ------------------

# Fixture example with database-style setup
'''
@pytest.fixture
def db_session():

    print("Opening database connection")

    session = create_database_session()

    yield session

    print("Closing database connection")

    session.close()
    # ------------------
    def test_create_employee(db_session):

    employee = Employee(
        name="Arun",
        email="arun@gmail.com"
    )

    db_session.add(employee)
    db_session.commit()

    assert employee.name == "Arun"
    '''
 #------------------

'''
Fixture scopes
------------------
Fixtures can also control how often they are created.

Common scopes:
---------------
function
class
module
package
session

The default is:

@pytest.fixture(scope="function")

It means the fixture runs for every test function.

Example
------------------
@pytest.fixture(scope="function")
def employee():
    return Employee("Arun", "arun@gmail.com", 50000)

'''
