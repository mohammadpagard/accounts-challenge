import re


class Account:
    __first_name = input("Enter you're first name: ")
    __last_name = input("Enter you're last name: ")

    def __init__(self, user_id, phone, email, username, password=None):
        self.username = self.__first_name + "_" + self.__last_name
        self.password = password
        self.user_id = user_id
        self.phone = phone
        self.email = email

    def show(self, username):
        username = username.replace('_', ' ')
        return f"{self.first_name} {self.last_name}"

    # Validations methods
    def password_validate(self):
        if len(str(self.password)) < 8:
            raise Exception("Invalid Password")
        else:
            self.password = hash(self.password)
            print(self.password)

    def phone_number_validate(self):
        if len(str(self.phone)) != 11:
            raise Exception("Invalid phone number")
        elif '09' not in self.phone[:2]:
            raise Exception("Invalid phone number")
        else:
            print(self.phone)

    def email_validate(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        def check(email_address):
            if re.fullmatch(regex, email_address):
                print(f"email address is {self.email}")
            else:
                raise Exception("Invalid email address")
        if __name__ == "__main__":
            email = self.email
            check(email)

    # Decorators
    def show_welcome(self):
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


a1 = Account(username='', password="Kmp981234", user_id='mohammadID', phone='09138159980', email='mohammadpagard2003@gmail.com')
# a1.phone_number_validate()
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
