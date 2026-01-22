class EmailValidator:
    def __init__(self,email):
        self.email= email;

    def validate(self):
        if "@" not in self.email or "." not in self.email:
            print("Not valid!")
        else:
            print("valid")
        return

    def get_domain(self):
        print(self.email.split("@")[-1])
    
email= input("Enter your email to check: ")
user_email= EmailValidator(email)
user_email.validate()
user_email.get_domain()
    