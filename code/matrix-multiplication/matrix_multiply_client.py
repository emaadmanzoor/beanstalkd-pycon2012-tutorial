#!/usr/bin/python

import beanstalkc
import memcache
# Config file having parameters the master and slave would use
import matconfig

print "Connecting to beanstalkd server.."
beanstalk = beanstalkc.Connection( '127.0.0.1', 11300 )

beanstalk.use( matconfig.JOBS )
beanstalk.watch( matconfig.ACKS )

mc = memcache.Client( ['127.0.0.1:11211'], debug=0 )

for i in range( matconfig.MATRIX_SIZE ):
    for j in range( matconfig.MATRIX_SIZE ):
        print 'Sending a row and column to job queue..'
        row = matconfig.MATRIX1[ i ]
        column = [ r[ j ] for r in matconfig.MATRIX2 ]
        stringRow = ' '.join( map( str, row ) )
        stringColumn = ' '.join( map( str, column ) )

        # Separating the row and column with a new line
        jobString = str( matconfig.MATRIX_SIZE * i ) + '\n' + str( j ) \
            + '\n' + stringRow + '\n' + stringColumn
        beanstalk.put( jobString )

print 'Sent all jobs to queue.'

# Each of the jobs returned would contain confirmation if
# Cij was completed
for i in range( matconfig.MATRIX_SIZE**2 ):
    job = beanstalk.reserve()
    print 'Confirmation: Worker finished computing C' + job.body

print 'All workers finished.'
print 'Extracting result from memory..'

print 'Got the result, Here it is: '
for i in range( matconfig.MATRIX_SIZE ):
    for j in range( matconfig.MATRIX_SIZE ):
        print ( mc.get( str( i*matconfig.MATRIX_SIZE + j ) ) ),
    print

