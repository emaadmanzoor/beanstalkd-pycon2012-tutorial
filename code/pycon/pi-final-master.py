# pi-final-master.py
#
# Training's done, lets kick some Pi 

import beanstalkc
import piconfig
import time

startTime = time.time()

beanstalk = beanstalkc.Connection(host='127.0.0.1', port=11300)
beanstalk.use(piconfig.JOBS)
beanstalk.watch(piconfig.ACKS)

dartsPerJob = int(piconfig.TOTALDARTS / piconfig.PARALLELISM)

for i in range(piconfig.PARALLELISM):
    print "Put job", i
    beanstalk.put(str(dartsPerJob), piconfig.DEADLINE)

totalCircleCount = 0
for i in range(piconfig.PARALLELISM):
    job = beanstalk.reserve()
    totalCircleCount += int(job.body)
    print "Received job", i, "circle count =", job.body
    job.delete()

pi = (4.0 * totalCircleCount) / (piconfig.TOTALDARTS)

print "Pi =", pi
print "Time taken:", str(time.time() - startTime), "seconds."
