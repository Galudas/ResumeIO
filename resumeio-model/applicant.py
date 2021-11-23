class Applicant:
    def __init__(self, experience, skills, name, email, position):
        self.experience = experience
        self.skills = skills
        self.name = name
        self.email = email
        self.position = position

    def __str__(self):
        return 'applicant(experience: ' + str(self.experience) \
               + ' \nskills:' + str(self.skills) \
               + ' \nname: ' + self.name \
               + ' \nemail: ' + self.email \
               + ' \nposition: ' + self.position + \
               ')\n'
