class User:
    def __init__(self, username) -> None:
        print(f"User created with username: {username}")
        self.username = username

    def getUsername(self):
        print(f"Username: {self.username}")