import json
class Database:

    def add_data(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        # below if elif avoid --> successful registrations even when we doesn't fill anything in the entry box
        if self.name == "":
            # Name is not mentioned
            return 2
        elif self.email == "":
            # email is not mentioned
            return 3
        elif self.password == "":
            # Password is not mentioned
            return 4

        with open('db.json', 'r') as f:
            database = json.load(f)

        if email in database:
            # If email already exists in the database
            return 0
        else:
            database[email] = [name, password] # Adding new registration details to the existing one
            with open('db.json', 'w') as wf:
                json.dump(database, wf)

            return 1

    def search(self, email, password):
        with open('db.json', 'r') as f:
            database = json.load(f)

        if email in database:
            if password == database[email][1]:
                return 0
                # Show options related to NLP
            else:
                # Incorrect password
                return 1
        else:
            # Incorrect email
            return 2