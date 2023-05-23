from effective import PredecessorGraph, Job

job1 = Job(name='job_1', release_time=2, deadline=10)
job2 = Job(name='job_2', release_time=0, deadline=7)

pred_graph = PredecessorGraph(init_job=[job1, job2])
pred_graph.append(predecessor='job_1',job=Job(name='job_3', release_time=1, deadline=12))
pred_graph.append(predecessor='job_2',job=Job(name='job_3', release_time=1, deadline=12))

pred_graph.append(predecessor='job_3',job=Job(name='job_4', release_time=4, deadline=9))
pred_graph.append(predecessor='job_3',job=Job(name='job_5', release_time=1, deadline=8))
pred_graph.append(predecessor='job_3',job=Job(name='job_7', release_time=6, deadline=21))

pred_graph.append(predecessor='job_4',job=Job(name='job_6', release_time=0, deadline=20))
pred_graph.append(predecessor='job_4',job=Job(name='job_7', release_time=6, deadline=21))

pred_graph.append(predecessor='job_5',job=Job(name='job_6', release_time=0, deadline=20))

pred_graph.description()

print('GET EFFECTIVE RELEASE TIME AND EFFECTIVE DEADLINES')
pred_graph.get_effective()
pred_graph.description()
