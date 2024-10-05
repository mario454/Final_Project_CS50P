class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.email = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
