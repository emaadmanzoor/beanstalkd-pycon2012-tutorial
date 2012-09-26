# pi-simple-master.py
#
# Our first master, does what a slave-driver does.

import beanstalkc

beanstalk = beanstalkc.Connection(host='127.0.0.1', port=11300)

for i in range(5):
    beanstalk.put('job for you')
