import time

from scheduler import Scheduler
from task import TaskInfo
from classifier_task import ClassifierTask

task0 = ClassifierTask(index=0)
task1 = ClassifierTask(index=1)
# task2 = TaskInfo(id=2)
# task3 = TaskInfo(id=3)

scheduler = Scheduler()
scheduler.SCH_Init()

scheduler.SCH_Add_Task(task0.run, 3000, 4000)
scheduler.SCH_Add_Task(task1.run, 1000, 2000)

# scheduler.SCH_Add_Task(task3.get_info, 2000, 3000)

# print('CALL EVENTS')
while True: 
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)

