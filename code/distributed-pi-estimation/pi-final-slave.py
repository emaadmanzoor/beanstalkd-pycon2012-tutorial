# pi-final-slave.py
#
# Training's done, let's kick some Pi 

import beanstalkc
import piconfig
import random

beanstalk = beanstalkc.Connection(host='127.0.0.1', port=11300)
beanstalk.watch(piconfig.JOBS)
beanstalk.use(piconfig.ACKS)

circleRadius = piconfig.SQEDGELEN / 2

while True:
    print "Waiting for work..."
    job = beanstalk.reserve()

    dartsToThrow = int(job.body)
    dartsInCircle = 0
    for i in range(dartsToThrow):
        x = (random.random() * piconfig.SQEDGELEN) - (piconfig.SQEDGELEN/2)
        y = (random.random() * piconfig.SQEDGELEN) - (piconfig.SQEDGELEN/2)
        if x ** 2 + y ** 2 <= circleRadius ** 2:
            dartsInCircle += 1
    
    beanstalk.put(str(dartsInCircle))

    print "Found", dartsInCircle, "out of", job.body, "darts within the circle."
    job.delete()
