class chatbook:

    __user_id = 0

    def __init__(self):
        self.__name = 'Default User'
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.username = ''
        self.password = ''
        self.login = False
        #self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id

    @staticmethod 
    def set_id(val):
        chatbook.__user_id = val

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to Proceed?
                                1. Press 1 to SignUp                   
                                2. Press 2 to SignIn                   
                                3. Press 3 to write a post
                                4. Press 4 to message a friend
                                5. Press any other key to exit
                           
                                -> """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sentMsg()
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
    
    def my_post(self):
        if self.login == True:
            txt = input('Enter Your message here: ')
            print(f"Following content has been posted-> {txt}")
        else:
            print("You need Signin first to post something")
            self.menu()

    def sentMsg(self):
        if self.login == True:
            txt = input("Enter Your Msg: ")
            frd = input("Whom to send the msg!")
            print(f"Your msg has been sent to your friend {frd}")
        else:
            print("You need to signin first to post something!")
            print("\n")
            self.menu()

user1 = chatbook()