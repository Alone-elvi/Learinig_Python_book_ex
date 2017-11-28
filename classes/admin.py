from classes.users import User
from classes.privilegies import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, age, privileges=0):
        super(Admin, self).__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)

# help(Admin)
