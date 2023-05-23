from copy import deepcopy

class Task:
    def __init__(self):
        self.job_list = []
        self.job_prototype_list = []

    def build_job(self, job):
        job_copy = deepcopy(job)
        return job_copy
    
    def reset_job(self, job):
        self.build_job(job)

