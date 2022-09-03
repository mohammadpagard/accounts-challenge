class Account:
    def __init__(self, user_id, phone, email, username=None, password=None):
        first_name = input("Enter you're first name please: ")
        last_name = input("Enter you're last name please: ")

        self.username = first_name + '_' + last_name
        self.password = password
        self.user_id = user_id
        self.phone = phone
        self.email = email

    def show_welcome(self):
        # Password validations
        if len(str(self.password)) < 8:
            raise Exception("Invalid Password!")
        else:
            self.password = hash(self.password)
            print(f"Username: {self.username}\nPassword: {self.password}")
        # Phone number validation
        if len(self.phone) != 11:
            raise Exception("Invalid phone number!")
        elif '09' not in self.phone[:2]:
            raise Exception("Invalid phone number!")
        else:
            print(f"Phone number: {self.phone}")
        # Email validation

    def verify_change_password(self):
        pass


a1 = Account(password="Kmp981234", user_id='mohammadID', phone='09138159980', email='mohammadpagard2003@gmail.com')
a1.show_welcome()


class Site:
    def __init__(self, url, register_users, active_users):
        self.url = url
        self.register_users = register_users
        self.active_users = active_users

    def register(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass
