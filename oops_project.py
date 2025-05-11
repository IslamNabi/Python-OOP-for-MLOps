class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.login = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to Proceed?
                                1. Press 1 to SignUp                   
                                2. Press 2 to SignIn                   
                                3. Press 3 to write a post
                                4. Press 4 to message a friend
                                5. Press any other key to exit""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter Your Email Here: ")
        password = input("Setup You Password Here: ")
        self.username = email
        self.password = password
        print("You have signed up Seuccessfully.")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print('Please Signup first by pressing 1 in main menu.')
        else:
            uname = input("Enter Your Email/Username here: ")
            pwd = input("Enter Your Password here: ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!")
                self.login = True
            else:
                print("Please enter correct credentials.")
        self.menu()

obj = chatbook()