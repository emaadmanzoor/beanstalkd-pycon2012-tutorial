# pi-efficient-slave.py
#
# Ramp up our efficiency; deadlines and dedicated queues

import beanstalkc
import piconfig

beanstalk = beanstalkc.Connection(host='127.0.0.1', port=11300)
beanstalk.watch(piconfig.JOBS)
beanstalk.use(piconfig.ACKS)

while True:
    job = beanstalk.reserve()
    beanstalk.put(job.body)
    print "Worked on job", job.body
    job.delete()
