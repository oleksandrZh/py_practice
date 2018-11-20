class Customer:
    def __init__(self, id, name, gender, birthdate, address, city, state, pin, mobile, email):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.address = address
        self.city = city
        self.state = state
        self.pin = pin
        self.mobile = mobile
        self.email = email


def get_valid_customer():
    customer = Customer(CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_GENDER,
                        CUSTOMER_BIRTHDATE, CUSTOMER_ADDRESS, CUSTOMER_CITY,
                        CUSTOMER_STATE, CUSTOMER_PIN, CUSTOMER_MOBILE, CUSTOMER_EMAIL)
    return customer


CUSTOMER_ID = 18868
CUSTOMER_NAME = 'TestQA'
CUSTOMER_GENDER = 'male'
CUSTOMER_BIRTHDATE = '2018-10-28'
CUSTOMER_ADDRESS = 'Test'
CUSTOMER_CITY = 'Test'
CUSTOMER_STATE = 'Test'
CUSTOMER_PIN = 123456
CUSTOMER_MOBILE = 123456789
CUSTOMER_EMAIL = 'test@valid.com'
