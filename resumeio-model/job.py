class Job:
    def __init__(self, description, department, requirements):
        self.description = description
        self.department = department
        self.requirements = requirements

    def __str__(self):
        return 'job(description: ' + str(self.description) \
               + ' \ndepartment:' + str(self.department) \
               + ' \nrequirements: ' + str(self.requirements) + \
               ')\n'
