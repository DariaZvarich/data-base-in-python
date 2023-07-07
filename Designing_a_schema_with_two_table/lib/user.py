class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
        
    def __eq__(self, other):
        return self._dict__ == other._dict__
    
    def __repe__(self):
        return f"User({self.id}, {self.username}, {self.email})"