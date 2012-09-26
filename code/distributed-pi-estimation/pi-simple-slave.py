# pi-simple-slave.py
#
# Our first slaves.

import beanstalkc

beanstalk = beanstalkc.Connection(host='127.0.0.1', port=11300)

job = beanstalk.reserve()
print job.body
