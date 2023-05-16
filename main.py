import time

from scheduler import Scheduler
from task import TaskInfo

task1 = TaskInfo(id=1)
task2 = TaskInfo(id=2)
task3 = TaskInfo(id=3)

scheduler = Scheduler()
scheduler.SCH_Init()

scheduler.SCH_Add_Task(task1.get_info, 1000, 2000)
scheduler.SCH_Add_Task(task2.get_info, 3000, 4000)
scheduler.SCH_Add_Task(task3.get_info, 2000, 3000)

print('CALL EVENTS')
while True: 
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)