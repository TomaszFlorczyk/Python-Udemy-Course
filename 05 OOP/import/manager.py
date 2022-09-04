from user import User, Employe

class Manager(Employe):
    def __init__(self, name):
        Employe.__init__(self, name)

    def __str__(self):
        return "Manager:" + self.name