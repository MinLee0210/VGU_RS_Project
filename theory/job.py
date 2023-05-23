class Job:
    def __init__(self, release_time=None, period=None, execution_time=None, relative_deadline=None, name='Job'):
        self.release_time = release_time
        self.period = period
        self.execution_time = execution_time
        if relative_deadline == None:
            self.relative_deadline = relative_deadline
        self.relative_deadline = relative_deadline
        self.name = name

    def description(self):
        message = f'Job: {self.name}\n'\
                f'>>> Release time: {self.release_time}\n'\
                f'>>> Execution time: {self.execution_time}\n'\
                f'>>> Relative Deadline: {self.relative_deadline}\n'\
                '======================================'
        print(message)