import re


class Account:
    first_name = input("Enter you're first name please: ")
    last_name = input("Enter you're last name please: ")

    def __init__(self, user_id, phone, email, username=None, password=None):
        self.username = self.first_name + '_' + self.last_name
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
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        def check(email_address):
            if re.fullmatch(regex, email_address):
                print(f"Email address: {self.email}")
            else:
                raise Exception("Invalid email address")

        if __name__ == '__main__':
            email = self.email
            check(email)
        # Print welcome and username validation
        upper_first_name = self.first_name[0].upper()
        upper_last_name = self.last_name[0].upper()
        print("\nWelcome to our site " + ''.join(upper_first_name + self.first_name[1:] + ' ' + upper_last_name + self.last_name[1:]))

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
