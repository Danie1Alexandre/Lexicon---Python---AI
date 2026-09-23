# Part A - Mutable default arguments

#1 --------

class BadTeam:
    def __init__(self, name, members = []): #bad
        self.name = name
        self.members = members 

    def add_member(self,member):
        self.members.append(member)

#2------
club1 = BadTeam("aik")
club2 = BadTeam("dif")

club1.add_member("anna")

print(club1.members) 
print(club2.members)
# anna added on both clubs, since both clubs uses the same list

# 3---------------

class GoodTeam:
    def __init__(self, name, members = None): #bad
        self.name = name
        if members == None:
            members = []
            
        self.members = members

    def add_member(self,member):
        self.members.append(member)

#4--------------
club1 = GoodTeam("aik")
club2 = GoodTeam("dif")

club1.add_member("anna")

print("good", club1.members) 
print(club2.members)

