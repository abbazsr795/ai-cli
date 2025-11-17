class Memory:

    def __init__(self, max_message=10):
        self.max_message = max_message
        self.messages = []

    def add(self, role, content):
        self.messages.append({"role" : role, "content" : content})
        if (len(self.messages) > self.max_message):
            self.messages.pop(0)

    def get(self):
        return self.messages