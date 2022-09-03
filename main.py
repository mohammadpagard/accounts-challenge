import re


class Account:
    first_name = input("Enter you're first name: ")
    last_name = input("Enter you're last name: ")

    def __init__(self, user_id, phone, email, username=None, password=None):
        self.username = self.first_name + "_" + self.last_name
        self.password = password
        self.user_id = user_id
        self.phone = phone
        self.email = email

    def show(self, username):
        username = username.replace('_', ' ')
        return f"{self.first_name} {self.last_name}"

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
        print("Welcome to our site ", end="")
        for user in self.username.split('_'):
            print(''.join(user.capitalize()), end=' ')

    def verify_change_password(self, old_password=None):
        old_password = input("\n\nEnter you're old password: ")
        if old_password == self.password:
            new_password1 = input("Enter you're new password: ")
            new_password2 = input("Enter again please: ")
            # Passwords match validation
            if new_password2 != new_password1:
                print("Passwords is not match!")
                new_password1 = input("Enter you're new password: ")
                new_password2 = input("Enter again please: ")
        else:
            raise Exception("Invalid old password")


a1 = Account(password="Kmp981234", user_id='mohammadID', phone='09138159980', email='mohammadpagard2003@gmail.com')
# a1.verify_change_password()
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
