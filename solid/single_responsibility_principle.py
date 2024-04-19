# This is a common violation of SRP


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        with open(f"{self.name}.txt", "w") as file:
            file.write(f"Name: {self.name}\nEmail: {self.email}")


# Usage
user = User("John Doe", "john.doe@example.com")
user.save()  # Saves user data to a file
