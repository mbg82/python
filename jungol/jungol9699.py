class SoccerTeam:
    def __init__(self, name, wop):
        self.name = name
        self.wop = int(wop)
    def print_team(self):
        print(self.name)

team = []

n,m = map(int,input().split())

for i in range(n):
    name,wop=input().split()
    j = SoccerTeam(name,wop)
    team.append(j)

for k in range(n):
    if team[k].wop >= m:
        team[k].print_team()

