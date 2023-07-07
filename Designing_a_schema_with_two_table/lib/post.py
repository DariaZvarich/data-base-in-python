class Post:
    def __init__(self, id, title, content, views, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.views = views
        self.user_id = user_id
        
    def __eq__(self, other):
        return self._dict__ == other._dict__
    
    def __repe__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.views}, {self.user_id} )"