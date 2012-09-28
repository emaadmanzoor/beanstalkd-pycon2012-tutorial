#!/usr/bin/python

import beanstalkc
import memcache
import time
import operator
import matconfig

while True:                             # Indefinitely wait for jobs to do

    print "Connecting to job server..."
    beanstalk = beanstalkc.Connection(host='127.0.0.1', port=11300)

    beanstalk.watch( matconfig.JOBS )     # Reserve jobs from this queue

    print "Waiting for jobs..."

    job = beanstalk.reserve()           # Blocks until a job is available

    print "Reserved a job.."

    [ strI, strJ, stringRow, stringColumn ] = job.body.split( '\n' )
    I = int( strI )
    J = int( strJ )
    row = map( int, stringRow.split() )
    column = map( int, stringColumn.split() )

    n = len( row )

    start_time = time.time()

    print 'Computing Cij..'
    try:
        result = reduce( operator.add, map( operator.mul, row, column ) )
    except Exception, e:
        print e
        print "Job failed.", n
        job.release()

    mc = memcache.Client ([ '127.0.0.1:11211' ], debug=0 )
    print 'Wrote result to',  str( I+J )
    mc.set( str( I + J ), result )
    beanstalk.use( matconfig.ACKS )
    beanstalk.put( strI + strJ )

    job.delete()                        # Tell the job server you're done
    beanstalk.close()

    print "Finished job in", str(time.time() - start_time), "seconds"
    print
