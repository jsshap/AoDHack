


class Participant:

    def _init__( self, email: str, name: str):
        self.email=email
        self.name=name

    def getEmail(self):
        return self.email

    def getName(self):
        return self.name