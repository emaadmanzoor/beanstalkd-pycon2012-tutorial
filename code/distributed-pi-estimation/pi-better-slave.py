# pi-better-slave.py
#
# A better slave, works until killed.

import beanstalkc

beanstalk = beanstalkc.Connection(host='127.0.0.1', port=11300)

while True:
    job = beanstalk.reserve()
    print job.body
