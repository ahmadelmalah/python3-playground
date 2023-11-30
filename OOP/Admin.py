from User import User

class Admin(User):
    def __init__(self, username) -> None:
        super().__init__(username)
        self.adminText = "This is a child attr"
    
    def getUsername(self):
        print(f"Admin username: {self.username}")

    def childMethod():
        pass