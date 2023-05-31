class SoftwareEngineer:
    def __init__(self, name: str):
        self.name = name
        self.skills = []

    def learn_skill(self, skill):
        self.skills.append(skill)



engineer = SoftwareEngineer("Max")
engineer.learn_skill("Python")

print(engineer.skills)