


class Participant:

    def __init__(self, email, name):
        self.email=email
        self.name=name

    def getEmail(self):
        return self.email

    def getName(self):
        return self.name

    def __str__(self):
        return (self.name + " (" + self.email + ")")

npar = Participant('frisboysproject@gmail.com','Sung')
print (npar)