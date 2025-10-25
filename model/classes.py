class UserModel:
    def __init__(self, id_user, user, password):
        self._id_user = id_user
        self._user = user
        self._password = password

    def get_id(self):
        return self._id_user
    
    def get_user(self):
        return self._user
    
    def get_password(self):
        return self._password
    
    def set_id(self, id=0):
        self._id_user = id

    def set_user(self, user):
        if len(user) < 5 and user != '':
            self._user = user 
    
    def set_password(self, password):
        if len(password) < 6 and password != '':
            self._password = password

class ProductModel:
    def __init__(self, id_product, product, price, quantity, registration_date):
        self._id_product = id_product
        self._product = product
        self._price = price
        self._quantity = quantity
        self._registration_date = registration_date

class SellModel:
    def __init__(self, id_sell, id_product, registration_date, total):
        self._id_sell = id_sell
        self._id_product = id_product
        self._registration_date = registration_date
        self._total = total