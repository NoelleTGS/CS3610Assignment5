

class Manual:
    def __init__(self):
        self.type = None
        self.instructions = ""

    def __str__(self):
        return f"Manual for {self.type}:\n{self.instructions}"