# pi-efficient-master.py
#
# Ramp up our efficiency; deadlines and dedicated queues

import beanstalkc
import piconfig

beanstalk = beanstalkc.Connection(host='127.0.0.1', port=11300)
beanstalk.use(piconfig.JOBS)        # Push here
beanstalk.watch(piconfig.ACKS)      # Listen here

for i in range(5):
    print "Put job", i
    beanstalk.put(str(i), piconfig.DEADLINE)

for i in range(5):
    job = beanstalk.reserve()
    print "Received job", i
