class User:
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        email = input('enter email')
        password = input('enter password')

        if email == self.email and password == self.password:
            login = True
            print('login successful!')
        else:
            print('login failed!')

    def logout(self):
        login = False
        print('logged out!')

    def function(self):