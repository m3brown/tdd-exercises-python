class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserManager:
    def __init__(self, user):
        self.user = user

    def save(self):
        with open(f"{self.user.name}.txt", "w") as file:
            file.write(f"Name: {self.user.name}\nEmail: {self.user.email}")


# Usage
user = User("John Doe", "john.doe@example.com")
manager = UserManager(user)
manager.save()  # Now the UserManager handles saving user data
