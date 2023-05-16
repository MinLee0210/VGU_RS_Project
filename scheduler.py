class Task:
    def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Delay = _Delay
        self.Period = _Period

    pTask = None
    Delay = 0
    Period = 0
    RunMe = 0
    TaskID = -1

class Scheduler:
    TICK = 1000
    SCH_MAX_TASKS = 40
    SCH_tasks_G = []
    current_index_task = 0
    def __int__(self):
        pass

    def SCH_Init(self):
        self.current_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.current_index_task
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")

    def SCH_Update(self):
        # for i in range(0, len(self.SCH_tasks_G)):
        #     if self.SCH_tasks_G[i].Delay > 0:
        #         self.SCH_tasks_G[i].Delay -= 1
        #     else:
        #         self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
        #         self.SCH_tasks_G[i].RunMe += 1

        if self.SCH_tasks_G[self.current_task].Delay > 0:
            self.SCH_tasks_G[self.current_task].Delay -= 1
        else:
            self.SCH_tasks_G[self.current_task].Delay = self.SCH_tasks_G[self.current_task].Period
            self.SCH_tasks_G[self.current_task].RunMe += 1
        # self.current_task = (self.current_task + 1) % len(self.SCH_tasks_G)

    def SCH_Dispatch_Tasks(self):
        # for i in range(0, len(self.SCH_tasks_G)):
        #     if self.SCH_tasks_G[i].RunMe > 0:
        #         self.SCH_tasks_G[i].RunMe -= 1
        #         self.SCH_tasks_G[i].pTask()

        if self.SCH_tasks_G[self.current_task].RunMe > 0:
            self.SCH_tasks_G[self.current_task].RunMe -= 1
            self.SCH_tasks_G[self.current_task].pTask()
        self.current_task = (self.current_task + 1) % len(self.SCH_tasks_G)

    def SCH_Delete(self, aTask):
        return

    def SCH_GenerateID(self):
        return -1
