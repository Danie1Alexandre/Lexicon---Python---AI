# Part A - Mutable default arguments

#1 

class BadTeam:
    def __init__(self, name, members = []): #bad
        self.name = name
        self.members = members

    def add_member(self,member):
        self.members.append(member)


club1 = BadTeam("aik")
club2 = BadTeam("dif")

club1.add_member("anna")

print(club1.members) # anna add on both
print(club2.members)